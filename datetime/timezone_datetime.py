from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2), "OSL")) #OPCIONAL COLOCAR O NOME, SE DEPOIS PRECISARMOS TRAZER O TZNAME, ELE TRAZ ESSE NOME QUE DECLARAMOS
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3), "BRT"))

print(data_oslo)
print(data_sao_paulo)
