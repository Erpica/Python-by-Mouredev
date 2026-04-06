print("\n1. Crea una variable con la fecha y hora actual.")
from datetime import datetime
current_datetime = datetime.now()

print("\n2. Imprime solo el año, mes y dí­a de la fecha actual.")
print(f"Año: {current_datetime.year}, mes: {current_datetime.month} y día: {current_datetime.day}.")

print("\n3. Crea una fecha especí­fica: 25 de diciembre de 2025 y muíéstrala.")
specific_date = datetime.strptime("2025-12-25", "%Y-%m-%d")
print(specific_date.strftime("%d/%m/%Y"))

print("\n4. Muestra solo la hora, los minutos y los segundos de un objeto time.")
from datetime import time
object_time = time(16, 41, 0)
print(object_time.hour, object_time.minute, object_time.second)

print("\n5. Calcula cuántos dí­as faltan para el 1 de enero del año siguiente.")
first_day_next_year = datetime.strptime(f"01/01/{current_datetime.year+1}", "%d/%m/%Y")
diff = first_day_next_year-current_datetime
print(diff.days)

print("\n6. Crea una función que reciba una fecha y devuelva su timestamp.")
def date_to_timestamp (date):
    return date.timestamp()

print(date_to_timestamp(current_datetime))

print("\nn7. Suma 30 dí­as a la fecha actual usando timedelta.")
from datetime import timedelta
day_plus_30 = current_datetime + timedelta(days=30)
print(datetime.strftime(day_plus_30, "%d/%m/%Y"))

# Ejemplo práctico para ver los días que quedan para la comunión. Cuando sean positivos para ver cuanto tiempo hace XD
print("Respecto a la comunión de Anto:")
comunion_day = datetime.strptime("18/04/2026", "%d/%m/%Y")
days_to_comunion = current_datetime - comunion_day
print(days_to_comunion)

print("\n8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 dí­as como simplificación).")
new_date = datetime.strptime("25/12/2026", "%d/%m/%Y")
new_day_plus_30 = new_date + timedelta(days=30)
print(datetime.strftime(new_day_plus_30, "%d/%m/%Y"))

# \n9. Compara dos fechas y muestra cuál es anterior.
date_1 = "10/10/2027"
date_2 = "05/05/2025"

obj_date_1 = datetime.strptime(date_1, "%d/%m/%Y")
obj_date_2 = datetime.strptime(date_2, "%d/%m/%Y")
if (obj_date_1.timestamp() - obj_date_2.timestamp() > 0):
    print(f"La fecha más antigua es: {datetime.strftime(obj_date_2, "%d/%m/%Y")}")
elif (obj_date_1.timestamp() - obj_date_2.timestamp() < 0):
    print(f"La fecha más antigua es: {datetime.strftime(obj_date_1, "%d/%m/%Y")}")
else:
    print(f"Has introducido la misma fecha: {datetime.strftime(obj_date_2, "%d/%m/%Y")}")

print("\nCreando mi propia función para mostrar fechas a mi manera:")
def my_date_format(date):
    print(datetime.strftime (date, "%d/%m/%Y"))

my_date_format(obj_date_1)

print("\n10. Crea una lista con varias fechas y ordíénalas cronológicamente.")
date_1 = "10/10/2027"
date_2 = "05/05/2025"
date_3 = "10/10/2020"
date_4 = "05/05/2030"
date_5 = "10/10/1980"
date_6 = "05/05/3000"

my_list = (datetime.strptime(date_1, "%d/%m/%Y"),
           datetime.strptime(date_2, "%d/%m/%Y"),
           datetime.strptime(date_3, "%d/%m/%Y"),
           datetime.strptime(date_4, "%d/%m/%Y"),
           datetime.strptime(date_5, "%d/%m/%Y"),
           datetime.strptime(date_6, "%d/%m/%Y")
           )
my_new_list = sorted(my_list) # O sorted(my_list, reverse=True)
for element in my_new_list:
    my_date_format(element)




