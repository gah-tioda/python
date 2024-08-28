import datetime

d = datetime.date(2023, 7, 19)
print(d) #2023-07-19

d = datetime.datetime(2023, 7, 19, 13, 45)
print(d) #2023-07-19 13:45:00

#algo muito comum é apenas importar a classe date

from datetime import date

data = date(2023, 7, 10)
print(data)

# A classe date tem os seguintes parâmetros:

# year, month, day

# YEAR tem <= 1 AND <= 9999
# MONTH tem <= 1 AND <= 12
# DAY tem <= 1 AND <= numero de dias no mes e ano fornecidos

date.today()

#Retorna a data local atual

