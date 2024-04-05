nome = "Gabriel"
idade = 23
profissao = "Analista de Dados"
linguagem = "Python"
saldo = 45.343

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}" .format(nome, idade))
print("Nome: {1} Idade: {0}" .format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome))
print("Nome: {name} Idade: {age} Nome: {name} {name}" .format(age=idade, name=nome))
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")

pessoa = {"nome": "Gabriel", "idade": 23, "profissao": "Analista de Dados", "linguagem": "Python"}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))