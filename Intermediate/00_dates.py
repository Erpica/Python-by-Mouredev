### Dates ###

from datetime import datetime

now = datetime.now()

'''
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
'''

def print_date (date):
    print(
        "date.year: ", date.year, 
        ", date.month: ", date.month, 
        ", date.day: ", date.day, 
        ", date.minute: ", date.minute, 
        ", date.second: ", date.second, 
        "\ndate.timestamp: ", date.timestamp
        )

print("Función print_date, variable now: ")
print_date(now)

year_2027 = datetime(2027, 1, 1)

print("\nyear_2027:")
print_date (year_2027)

# De objeto a Texto (Formatear)
print("\nstrftime:")
print(now.strftime("%d/%m/%Y %H:%M"))

# De Texto a Objeto (Parsear). Convierte una fecha en un objeto para trabajar con él.
text_date = "2027-01-01"
object_date = datetime.strptime(text_date, "%Y-%m-%d")

from datetime import time
current_time = time(14, 30, 0)
print(
    "\ncurrent_time.hour", current_time.hour,
    "\ncurrent_time.minute", current_time.minute,
    "\ncurrent_time.second: ", current_time.second
    )


from datetime import date

current_date = date.today()
print(
    "current_date.year: ", current_date.year,
    "//current_date.month: ", current_date.month,
    "//current_date.day: ", current_date.day
)

current_date = date(2011, 3, 31)
print(
    "current_date.year: ", current_date.year,
    "// current_date.month: ", current_date.month,
    "// current_date.day: ", current_date.day
)

# Operaciones con fechas:
current_date = date(current_date.year + 15, current_date.month, current_date.day)
print(
    "current_date.year: ", current_date.year,
    "// current_date.month: ", current_date.month,
    "// current_date.day: ", current_date.day
)

diff = year_2027 - now
print(diff)
diff = year_2027.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print (end_timedelta - start_timedelta)
print (end_timedelta + start_timedelta)

