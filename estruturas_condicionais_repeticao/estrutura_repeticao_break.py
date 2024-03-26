while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

# É possível usar com for também
    
for numero in range(100):

    if numero == 10:
        break

    print(numero, end=" ")

#uso do continue, exemplo de programa para apenas exibir números ímpares

for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")
    