produto_1 = 20
produto_2 = 10

soma = produto_1 + produto_2
subtracao = produto_1 - produto_2
divisao = produto_1 / produto_2
divisao_int = produto_1 // produto_2
multiplicacao = produto_1 * produto_2
exponenciacao = produto_1 ** produto_2
modulo = produto_1 % produto_2

print("Soma = " + str(soma), end="\n")
print("Subtração = " + str(subtracao), end="\n")
print("Divisão = " + str(divisao), end="\n")
print("Divisão inteira = " + str(divisao_int), end="\n")
print("Multiplicação = " + str(multiplicacao), end="\n")
print("Exponenciação = " + str(exponenciacao), end="\n")
print("Módulo = " + str(modulo), end="\n")

#Precedência matemática
"""
Nesses casos, é uma boa prática sempre deixarmos explícito com os parentêses quais as operações que serão processadas antes.

"""

x = (10 + 5) * 4
y = (10 / 2) + (25 * 2) - (2 ** 2)

print("Valor de X = " + str(x), end="\n")
print("Valor de Y = " + str(y), end="\n")