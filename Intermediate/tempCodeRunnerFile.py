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
    print("date.year: " + date.year + "date.month: " + date.month)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp)

print("Función print_date, variable now: ")
print_date(now)