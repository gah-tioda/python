from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_pt_br = '%d/%m/%Y %a' #converte para este padrão de data + dia semana
mascara_en = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_pt_br))

data_convertida = datetime.strptime(data_hora_str, mascara_en)

print(data_convertida)
print(type(data_convertida))