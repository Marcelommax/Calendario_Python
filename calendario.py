import calendar
from datetime import date

data = date.today()

print(data)

ano = int('{}'.format(data.year))

mes = int('{}'.format(data.month))


monthRange = calendar.monthrange(ano, mes)
print(monthRange)

for  dias in range(1, monthRange[-1]+1):
	print (dias)
