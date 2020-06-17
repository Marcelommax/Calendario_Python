import calendar

ano = 2020

mes = 6

calendario = calendar.month(ano, mes) 

print(calendario.split())


monthRange = calendar.monthrange(ano, mes)
print(monthRange)
