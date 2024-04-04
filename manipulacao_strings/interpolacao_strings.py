pessoa = {"nome": "Gabriel", "idade": 23, "profissao": "Analista de Dados", "linguagem": "Python"}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))