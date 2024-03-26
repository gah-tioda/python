texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end="")
    else: 
        print(f"Letra {texto} não existe")

print() #adiciona uma quebra de linha