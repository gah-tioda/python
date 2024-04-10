
# Strings e Fatiamento com Python

Este documento explicará métodos úteis para manipular objetos do tipo string, como interpolar valores de variáveis e entender o funcionamento do fatiamento. 

### _Métodos úteis da classe_ `str`

A classe string do Python é rica em métodos e possui uma interface simples de trabalhar. 

- Maiúscula, minúscula e título

~~~python
curso = "pYtHon"

#Converte para maiúscula
print(curso.upper())
>>> PYTHON

#Converte para minúscula
print(curso.lower())
>>> python

#Deixa apenas a primeira letra maiúscula
print(curso.title())
>>> Python
~~~

- Eliminando espaços em branco

~~~python
curso = "  Python "

#Remove os espaços tanto da direita quanto da esquerda
print(curso.strip())
>>> "Python"

#Remove o espaço da esquerda
print(curso.lstrip())
>>> "Python "

#Remove o espaço da direita
print(curso.rstrip())
>>> "  Python"
~~~

- Junções e centralização

~~~python
curso = "Python"

#Acrescenta valores (ou espaços em branco) dentro de um conjunto máximo de caracteres definidos na função e centraliza a palavra no centro.

print(curso.center(10, "#"))
>>> "##Python##"

#o join funciona com qualquer tipo iterável. Neste caso ele vai percorrer cada letra da palavra e incluir um ponto depois da letra.

print(".".join(curso))
>>> "P.y.t.h.o.n"
~~~

### _Interpolação de Strings_

Existem 3 formas de interpolar variáveis com o Python 3: usando o sinal `%`, o método `format` ou `f strings`.

A primeira forma não é atualmente recomendada e seu uso em Python 3 é rara, por esse motivo, focaremos nas duas últimas. 

- Old style `%`

OBS: Utiliza-se `%s` para valores string, `%d` para valores inteiros e `%f` para valores com ponto flutuante (float).

Após a mensagem, incluir o % e dentro dos parênteses informar as variáveis na ordem correta.

Essa abordagem é negativa pois em casos mais complexos, pode ficar uma lista muito grande de variáveis declaradas ou até mesmo inverter a ordem correta e o resultado ser diferente do esperado.

~~~python
nome = "Gabriel"
idade = 23
profissao = "Analista de Dados"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

>>> Olá, me chamo Gabriel. Eu tenho 23 anos de idade, trabalho como Analista de Dados e estou matriculado no curso de Python.
~~~

- Método `format`

O primeiro exemplo é bem parecido com o Old style, não sendo tão vantajoso ainda. Na segunda opção, o format nos traz uma vantagem de, mesmo fora de uma sequência, podemos declarar a posição correta da variável que contém o valor. 

Um exemplo que pode ser útil é quando precisamos usar a mesma variável em vários pedaços da mensagem, assim, basta apenas informar o número entre as chaves.

O terceiro exemplo usamos o format com argumentos nomeados, ou seja, entre as chaves declaramos um nome/identificador e nos argumentos da função, precisamos passar a variável que contém o valor = nome que declaramos entre as chaves como identificador.

~~~python
nome = "Gabriel"
idade = 23
profissao = "Analista de Dados"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))

#Argumentos com valor posicional

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}." .format(linguagem, profissao, idade, nome))

#Argumentos de forma nomeada

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#Argumentos com dicionário 

pessoa = {"nome": "Gabriel", "idade": 23, "profissao": "Analista de Dados", "linguagem": "Python"}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))

>>> Olá, me chamo Gabriel. Eu tenho 23 anos de idade, trabalho como Analista de Dados e estou matriculado no curso de Python.
~~~

- `f-string`

Não é necessário mais usar o .format, basta colocar um "f" no começo da string e declarar entre as chaves as variáveis que contém o valor. Esse tipo garante maior legibilidade do código.

~~~python
nome = "Gabriel"
idade = 23
profissao = "Analista de Dados"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

>>> Olá, me chamo Gabriel. Eu tenho 23 anos de idade, trabalho como Analista de Dados e estou matriculado no curso de Python.
~~~

- Formatar strings com `f-string`

Este caso é muito útil ao trabalhar com valores com casas decimais.

~~~python
pi = 3.14159

#Espaço em branco antes do "." não acrescenta espaços em branco e mantém o valor que estiver.

print(f"Valor de PI: {pi: .2f}")
>>> "Valor de PI: 3.14"

#Valor antes do "." acrescenta espaços em branco e mantém o valor que estiver.

print(f"Valor de PI: {pi:10.2f}")
>>> "Valor de PI:            3.14"
~~~

### _Fatiamento de Strings_

O fatiamento de strings é uma técnica que retorna substrings (partes da string original), informando início (start), fim (stop) e passo (step): [start: stop[,step]]

~~~python
nome = "Gabriel Antonini"

nome[0]
>>> "G"

nome[:8]
>>> "Gabriel"

nome[8:]
>>> "Antonini"

nome[8:12]
>>> "Anto"

nome[8:14:2]
>>> "Atn"

nome[:]
>>> "Gabriel Antonini"

#Invertida
nome[::-1]
>>> "ininotnA leirbaG"

#Última letra string
nome[-1]
>>> "i"
~~~

### _Strings de múltiplas linhas_

São definidas quando usamos 3 aspas simples ou duplas durante a atribuição. Podem ocupar várias linhas de código e todos os espaços em branco são incluídos na string final (quebras de linha, espaços maiores entre palavras, etc.)

~~~python
nome = "Gabriel"

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
"""
mensagem_aspas_simples = f'''
Olá meu nome é {nome},
Eu estou aprendendo Python
'''
~~~