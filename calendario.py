import calendar
from datetime import date

data = date.today()

print(data)

ano = int('{}'.format(data.year))

mes = int('{}'.format(data.month))


#calendario = calendar.month(ano, mes) 

#fatiar = calendario.split()

#print(fatiar[9:-1])


monthRange = calendar.monthrange(ano, mes)
print(monthRange)

for  dias in range(1, monthRange[-1]+1):
	print (dias)
