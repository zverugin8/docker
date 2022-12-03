import calendar
print('Welcome to calendar\n')
year = int(input('Enter the year: '))
#month = int(input('Enter the month: '))
for month in range(1,13):
    print(calendar.month(year,month), end='')
print('Bye!')