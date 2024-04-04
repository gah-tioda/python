
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