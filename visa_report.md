# Отчёт: бесконечный цикл ошибок в lib_visa (ESP32Comm.send_command)

Дата: 2026-09-18
Файл: `lib_visa/mc_usb/esp32.py`, класс `ESP32Comm`, метод `send_command`

## Суть проблемы

Транспортный уровень копил ошибки и никогда не возвращал управление:

```python
# БЫЛО
answer = self._simple_send_command(command)
while "ERR" in answer or "Err" in answer:
    answer = self._simple_send_command('NNNN')
    answer = self._simple_send_command(command)
return answer
```

Три дефекта складывались в бесконечный цикл:

1. **Нет счётчика попыток.** Цикл `while "ERR" in answer` повторялся
   неограниченно — команда `par1:111000` шлётся снова и снова.

2. **`NNNN` не поддерживается прошивкой.** Лог стенда:
   `Send: NNNN, Response: ['ERR invalid:000']`. Ответ тоже содержит
   `"ERR"` → условие цикла остаётся истинным. `NNNN` был задуман как
   команда ресинхронизации, но текущая прошивка ESP32 его не знает —
   каждый круг даёт две бесполезные транзакции вместо одной.

3. **Пустой ответ превращается в `"Error: no response"`, которое тоже
   содержит `"Err"`.** Когда ESP перестаёт отвечать, `_simple_send_command`
   возвращает `"Error: no response"` → условие цикла снова истинно → цикл
   не завершается даже при полном молчании порта (~1.1 с на круг).

В результате при первой же ошибке прошивки (например,
`ERR par:1:111:AssertionError`) программа навсегда зависала внутри
`send_command`, не доходя до `_check_asp`/`_check_esp` в прикладном коде,
и единственным выходом был внешний сторож-таймаут.

## Исправление

```python
# СТАЛО
class ESP32Comm:
    MAX_SEND_ATTEMPTS = 3

    def send_command(self, command: str) -> str:
        if not self._serial or not self._serial.is_open:
            return "Error: not connected"

        self._serial.write(f"{command}\n".encode())
        self._serial.flush()

        answer = self._simple_send_command(command)
        attempts = 0
        while "ERR" in answer or "Err" in answer:
            attempts += 1
            if attempts >= self.MAX_SEND_ATTEMPTS:
                return answer  # отдаём последний ответ (с ошибкой) вызывающему коду
            time.sleep(0.1)
            answer = self._simple_send_command(command)
        return answer
```

Что изменено:

- **Повторов не более `MAX_SEND_ATTEMPTS = 3`** — короткая транзиентная
  ошибка (глюк порта, занятый ESP) ещё имеет шанс пройти, зацикливание —
  нет.
- **`NNNN` убран** — прошивка его не поддерживает, пользы нет, вреда два
  лишних оборота ожидания.
- **По исчерпании попыток возвращается последний ответ (с текстом ошибки)**
  вызывающему коду — управление возвращается всегда.

## Как теперь течёт ошибка

1. `send_command` → максимум 3 попытки → возвращает `ERR ...` или
   `Error: no response`.
2. `_check_esp` (meas.py) видит `Error`/`ERR` → `RuntimeError` с точным
   местом (операция, ответ ESP).
3. `retry` (meas.py) — до 3 повторов шага с паузой.
4. Не помогло → `SystemExit(3)` → выход из `with` → `__exit__` DP832A
   гарантированно выключает питание.

Проверено эмуляцией: при постоянной ошибке/тишине прошивки выполняется
ровно 3 вызова, `NNNN` не отправляется, метод возвращает ответ с ошибкой.
