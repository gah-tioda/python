saldo = 450
saque = 200

igualdade = saldo == saque
diferenca = saldo != saque
maior = saldo > saque
maior_igual = saldo >= saque
menor = saldo < saque
menor_igual = saldo <= saque

print(igualdade, end="\n")
print(diferenca, end="\n")
print(maior, end="\n")
print(maior_igual, end="\n")
print(menor, end="\n")
print(menor_igual, end="\n")

if igualdade == True:
    print("Os valores de saldo e saque são iguais", end="\n")
else:
    print("Os valores de saldo e saque não são iguais", end="\n")

if diferenca == True:
    print("Os valores de saldo e saque são diferentes", end="\n")
else:
    print("Os valores de saldo e saque não são diferentes", end="\n")    

if maior == True:
    print("O valor de saldo é maior que saque", end="\n")
else:
    print("O valor de saldo é menor que saque", end="\n") 

if maior_igual == True:
    print("O valor de saldo é maior ou igual à saque", end="\n")
else:
    print("O valor de saldo é menor ou igual à saque", end="\n") 

if menor == True:
    print("O valor de saldo é menor que saque", end="\n")
else:
    print("O valor de saldo é maior que saque", end="\n") 

if menor_igual == True:
    print("O valor de saldo é menor ou igual à saque", end="\n")
else:
    print("O valor de saldo é maior ou igual à saque", end="\n") 