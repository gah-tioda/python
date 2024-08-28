import datetime

#convertendo string para datetime

date_string = "20/07/2023 15:30"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d) #2023-07-20 15:30:00