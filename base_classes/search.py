import pyvisa
rm = pyvisa.ResourceManager()

try:
    resources = rm.list_resources()
    print("Доступные ресурсы:")
    for resource in resources:
        print(f"\nРесурс: {resource}")
        try:
            instrument = rm.open_resource(resource)
            instrument.timeout = 1000
            instrument.encoding = 'utf-8'
            idn = instrument.query('*IDN?')
            print(f"IDN: {idn.strip()}")
        except Exception as e:
            print(f"Ошибка при работе с ресурсом: {e}")
        finally:
            if instrument:
                instrument.close()
finally:
    rm.close()


