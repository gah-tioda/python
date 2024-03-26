
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

- Operadores de atribuição

Utilizados para definir valor inicial ou sobreescrever um valor de uma variável. 

_Atribuição simples_

~~~python
#Atribui apenas um valor à uma variável
saldo = 500

print(saldo)
>>> 500
~~~

_Atribuição com adição_

~~~python
#Atribui um valor à uma variável saldo e adicionei mais 200
saldo = 500
saldo += 200

print(saldo)
>>> 700
~~~

_Atribuição com subtração_

~~~python
#Atribui um valor à uma variável saldo e subtrai 200
saldo = 500
saldo -= 200

print(saldo)
>>> 300
~~~

_Atribuição com multiplicação_

~~~python
#Atribui um valor à uma variável saldo e multiplica por 2
saldo = 500
saldo *= 2

print(saldo)
>>> 1000
~~~

_Atribuição com divisão_

~~~python
#Atribui um valor à uma variável saldo e divide por 5
saldo = 500
saldo /= 5

print(saldo)
>>> 100.0

#divisão inteira
saldo = 500
saldo //= 5

print(saldo)
>>> 100
~~~

_Atribuição com módulo_

~~~python
#Atribui um valor à uma variável saldo divide por 8 e retorna o resto da divisão
saldo = 500
saldo %= 480

print(saldo)
>>> 20
~~~

_Atribuição com exponenciação_

~~~python
#Atribui um valor à uma variável saldo e eleva ao quadrado
saldo = 80
saldo **= 2

print(saldo)
>>> 6400
~~~

- Operadores lógicos 

Operadores utilizados em conjunto com operadores de comparação, para montar uma expressão lógica. O resultado da comparação é um valor booleano.

_Operador E_

- Ambas as operações precisam ser verdadeiras para retornar `True`, senão, `False`

~~~python
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
>>> False
~~~

_Operador OU_

- Uma das operações precisa ser verdadeira para retornar `True`, senão, `False`

~~~python
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
>>> True
~~~

_Operador Negação_

- Utiliza-se o `not` para negar uma expressão resultando em um valor inverso ao real. 

~~~python
contatos_emergencia = []

not 1000 > 500
>>> True

#Listas vazias no Python tem o valor default False (sequências vazias)
not contatos_emergencia 
>>> True

not "saque 1500;"
>>> False

#Strings vazias no Python tem o valor default False (sequências vazias)
not ""
>>> True
~~~

_Parênteses_

- Assim como os operadores aritméticos, os parênteses indicam a precedência, ou seja, que operações serão realizadas antes (mesma lógica, da esquerda para direita). 

~~~python
saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
>>> True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
>>> True
~~~

- Operadores de identidade 

Operadores de identidade são usados para comparar se dois objetos testados ocupam a mesma posição na memória. Utiliza-se o `is` ou `is not` para negar e realmente confirmar se ele ocupa a posição da memória.

_Exemplo_

~~~python
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
>>> True

curso is not nome_curso
>>> False

saldo is limite
>>> True
~~~

- Operadores de associação 

Operadores de associação são usados para verificar se um objeto está presente em uma sequência.

_Exemplo_

Usamos o `in` para verificar se algo está na sequência ou `not in` para verificar se não está.
Lembrando que ele é case sensitive, ou seja, se na sequência conter uma palavra que algum caractere é maiúsculo, se pesquisarmos totalmente com minúsculo, ele retornará como `False`

~~~python
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso
>>> True

"maçã" not in frutas
>>> True

200 in saques
>>> False
~~~