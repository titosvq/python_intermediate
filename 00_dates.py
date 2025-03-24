### Fechas ###

import datetime # Hay que importar el módulo correspondiente

# Representación de una hora, un día

now = datetime.datetime # Llamamos al módulo y a la función de su nombre propio


# Otra forma de llamar al módulo: 

from datetime import datetime

now = datetime.now()
print(now)

def print_date(date): # Definimos la función print_date, la llamamos más adelante
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print("Referencia holaaaaa")

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


# Trabajamos con la función creada al principio:

print_date(now)

timestamp = now.timestamp() # Representación numérica del momento concreto, de un tiempo
print(timestamp)

year_2026 = datetime(2026, 1, 1)

print_date(year_2026)

print("Cambio")


# Importamos ahora time

from datetime import time

current_time = time(12, 34, 23) # A secas printea ceros, es un ojeto que nos sirve para encapsular tiempo, hay que rellenarlo con valores dentro de los paréntesis

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


# Importamos date

print("Cambio")

from datetime import date

# current_date = date() # A secas da error, hay que definir los datos en los paréntesis

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday()) # Hay que llamar weekday con paréntesis del 0 lunes al 6 domingo

current_date = date(1988, 10, 14)

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday()) 


# Vamos a intentar modificar los datos aplicando operaciones

current_date = date(1988, 3, 25)

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday()) 

current_date = date(current_date.year, current_date.month + 2, current_date.day + 3) # De esta forma podemos hacer operaciones 
print(current_date.month, current_date.day)

diff = year_2026 - now # Otra forma de operar, pero hay que asegurarse que las fechas están definidas con el mismo tipo de objeto
print(diff)

diff = year_2026.date() - current_date # Habría que ver porque sale el resultado que sale, pero funciona
print(diff)

print("Continúa la ejecución")

# Importamos timedelta que nos permite operar con diferentes fechas

from datetime import timedelta

time_delta = timedelta()

init_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta) # Es para trabajar con franjas de fechas     