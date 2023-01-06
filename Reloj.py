import time
def set_clock(hour, minute):
    while True:
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        if current_hour == hour and current_minute == minute:
            print("¡Son las", hour, ":", minute, "en el reloj!")
            break
        else:
            print("Esperando a que sea", hour, ":", minute, "en el reloj...")
            time.sleep(60)
hour = int(input("Ingresa la hora (formato 24h): "))
minute = int(input("Ingresa los minutos: "))
set_clock(hour, minute)