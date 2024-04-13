def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar) # O resultado da operação é = 20
exibir_resultado(10, 10, subtrair) # O resultado da operação é = 0

'''No exemplo abaixo vemos que se utilizassemos um append diretamente na variável dentro da função (local)
consequentemente atualizaria a variável externa (global). Para contornar isso, criamos uma cópia da lista global
para que as alterações apenas reflitam na cópia localmente.
'''

salario = 2000

def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")

    salario += bonus
    return salario


lista = [1]
salario_com_bonus = salario_bonus(500, lista) # 2500

print(salario_com_bonus)
print(lista)