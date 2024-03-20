
# Operadores em Python

- Operadores Aritméticos

Executam operações matemáticas como adição, subtração, multiplicação, etc.

_Adição, subtração e multiplicação_
~~~python
#Adição
print(1 + 1)
>>> 2

#Subtração
print(10 - 2)
>>> 8

#Multiplicação
print(4 * 3)
>>> 12
~~~

_Divisão e divisão inteira_
~~~python
#Divisão
print(12 / 3)
>>> 4.0

#Divisão inteira
print(12 // 2)
>>> 6
~~~

_Módulo e exponenciação_

**Módulo**: retorna o resto de uma divisão como resultado

~~~python
#Módulo
print(10 % 3)
>>> 1

#Exponenciação
print(2 ** 3)
>>> 8
~~~

**Precedência de operadores**

Na matemática, existe uma regra que indica quais operações devem ser executadas primeiro. Dependendo da ordem das operações, o valor pode ser diferente. 

_x = 10 - 5 * 2_ 

_x é igual a 10 ou 0?_

Devemos seguir a seguinte ordem:

- Parênteses;
- Expoentes; 
- Multiplicações e divisões (da esquerda para a direita);
- Somas e subtrações (da esquerda para a direita)

Exemplos:

~~~python
print(10 - 5 * 2)
>>> 0

print((10 - 5) * 2)
>>> 10

print(10 ** 2 * 2)
>>> 200

print(10 ** (2 * 2))
>>> 10000

print(10 / 2 * 4)
>>> 20.0
~~~

Nesses casos, é uma boa prática sempre deixarmos explícito com os parentêses quais as operações que serão processadas antes.

~~~python
x = (10 + 5) * 4
y = (10 / 2) + (25 * 2) - (2 ** 2)

print("Valor de X = " + str(x), end="\n")
print("Valor de Y = " + str(y), end="\n")

>>>Valor de X = 60
Valor de Y = 51.0
<<<<<<< HEAD
=======
~~~

- Operadores de Comparação

Operadores utilizados para comparação de valores (dois valores ou mais).

O retorno das comparações é sempre um valor _bool_ (booleano - `True` ou `False`)

Tipo   | Sinal
--------- | ------
Igualdade | `==`
Diferença | `!=`
Maior | `>`
Maior ou igual | `>=`
Menor | `<`
Menor ou igual | `<=`

**Exemplos**:

_Igualdade_
~~~python
saldo = 450
saque = 200

print(saldo == saque)
>>> False
~~~

_Diferença_
~~~python
saldo = 450
saque = 200

print(saldo != saque)
>>> True
~~~

_Maior que/ maior ou igual_
~~~python
saldo = 450
saque = 200

print(saldo > saque)
>>> True

print(saldo >= saque)
>>> True
~~~

_Menor que/ menor ou igual_
~~~python
saldo = 450
saque = 200

print(saldo < saque)
>>> False

print(saldo <= saque)
>>> False
~~~
