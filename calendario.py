import calendar

ano = 2020

mes = 2

#calendario = calendar.month(ano, mes) 

#fatiar = calendario.split()

#print(fatiar[9:-1])


monthRange = calendar.monthrange(ano, mes)
print(monthRange)

for  dias in range(1, monthRange[-1]+1):
	print (dias)
