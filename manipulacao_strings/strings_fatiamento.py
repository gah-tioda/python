#Trabalhar com strings

nome = "gAbRieL"

print(nome.upper())
print(nome.lower())
print(nome.title())

#Remover espaços em branco

texto = "   Olá mundo!    "

print(texto)
print(texto.strip() + ".")
print(texto.lstrip()+ ".")
print(texto.rstrip()+ ".")

#Junção e centralização

menu = "Python"

print("####" + menu + "####") #como gostaríamos que ficasse
print(menu.center(14))
print(menu.center(14, "#")) #forma mais simples de ter o mesmo resultado

print("P-y-t-h-o-n")

#Exemplo usando um for

for letra in menu:
    print(letra, end="-")
print()

#Exemplo usando o join

print("-".join(menu))

#Fatiamento

nome_2 = "Gabriel Antonini"

print(nome_2[0])

print(nome_2[:8])

print(nome_2[8:])

print(nome_2[8:12])

print(nome_2[8:14:2])

print(nome_2[:])

print(nome_2[::-1])

print(nome_2[-1])
