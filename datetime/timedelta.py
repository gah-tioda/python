# d = datetime.datetime(2023, 7, 19, 13, 45)
# print(d) #2023-07-19 13:45:00

# #adicionando uma semana
# #classe timedelta
# d = d + datetime.timedelta(weeks=1)
# print(d) #2023-07-26 13:45:00

# import datetime
from datetime import date, datetime, time, timedelta

tipo_carro = 'P' #P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')

#Eu posso trabalhar com valores altos também à serem acrescentados ou diminuídos.

#Eu não consigo realizar as operações abaixo pois é necessário um valor de data + hora para manipular
#com timedelta

# print(date.today() - timedelta(days=1))

# print(time(10, 19, 20) - timedelta(hours=1))

#Uma solução é criar um valor de datetime completo e na visualização extrair a parte desejada
#seja apenas hora ou o valor de data

resultado = print(datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1))
print(resultado.time())
print(datetime.now().date())
