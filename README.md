
# Conhecendo a Linguagem Python 

Este conteúdo foi criado seguindo o curso de Python da [Dio](dio.me) para o Bootcampo de Python Data Analytics da Squadio.

## Tipos de Dados

- O que são tipos?

Servem para definir as características de um valor (objeto) para o interpretador. 

Exemplo: 

_Com um determinado tipo, posso realizar operações matemáticas_;

_X tipo de dado consome 24 bytes de armazenamento_

- Tipos Built-in mais comuns 

| Tipo  | Representação |
| ------------- | ------------- |
| Texto  | str  |
| Numérico  | int, float, complex  |
| Sequência | list, tuple, range |
| Mapa (chave-valor) | dict |
| Coleção (não permitem valores repetidos)| set, fronzenset |
| Booleano | bool |
| Binário | byes, bytearray, memoryview |

## Modo interativo

- Como iniciar?

Modo em que na medida que escrevemos o código ele executa. 

Podemos digitar "python" ou executar nosso script com o flag -i (python -i app.py)

- funções _dir_ e _help_

A função dir, sem argumentos, retorna a lista de nomes no escopo local atual. Com argumento, retorna uma lista de atributos (métodos) que podem ser usados com o objeto, ou aquele tipo de dados.

A função help retorna a documentação em relação ao objeto.

## Variáveis e constantes

- Variáveis

Em linguagens de programação, ao definir valores, podemos alterá-los. Ou seja, os dados podem ser alterados ao longo da execução. Isso são variáveis.

- Constantes

São registros que os valores atribuídos são imutáveis, ou seja, nascem com um valor e permanece aquele valor até o fim. 

Python não possui constantes. Em algumas linguagens como Java (termo _final_) e C (termo _const_), podemos declarar constantes.

Existe uma convenção que diz quando uma variável é constante: declaramos o nome dela como MAIÚSCULO.

- Boas práticas

Declarar variáveis em _snake case_ (fulano_tal), substituir espaços em branco por underline;

Escolher nomes sugestivos, ou seja, nomes que se associam ao o que significa aquele valor armazenado. Exemplo: limite_saque = 500

Nome em MAIÚSCULO se for valor constante

- Exemplos em código:

~~~python
nome = "Guilherme"
idade = 28
nome, idade = "Guilherme", 28
~~~

~~~python
BRAZILIAN_STATES = ["SP", "MG", "RJ"]
~~~

## Conversão de Tipos

- Em que casos usar?

Momentos que precisamos converter o tipo de valor de uma variável para manipular de uma forma diferente. Exemplo: uma variável do tipo _string_ que recebe valor numérico e precisamos realizar operações matemáticas.

- _int_ para _float_

~~~python
preco = 10
print(preco)
>>> 10

preco = float(preco)
print(preco)
>>> 10.0
~~~

Divisão de valores sempre resultam em _float_

~~~python
preco = 10/2
print(preco)
>>> 5.0
~~~

- _float_ para _int_

~~~python
preco = 10.30
print(preco)
>>> 10.3

preco = int(preco)
print(preco)
>>> 10
~~~

- Conversão por divisão

Existe um caso que se dividirmos um valor usando duas barras (//) ele preserva o número inteiro como resultado. 

~~~python
preco = 10 // 2
print(preco)
>>> 5
~~~

- Numérico para String (_str_)

~~~python
preco = 10.50
idade = 28

print(str(preco))
>>> 10.5

print(str(idade))
>>> 10.5
~~~

Temos um caso que podemos utilizar a interpolação de strings para trabalhar com valores mutáveis, basta colocarmos o f antes da string e as variáveis entre {}, conforme exemplo:

~~~python 
texto = f" idade {idade} preco {preco}"
print(texto)
>>> idade 28 preco 10.5
~~~

- String para número

~~~python 
preco = "10.50"
idade = "28"

print(float(preco))
>>> 10.50

print(int(idade))
>>> 28
~~~

- Erro de Conversão

O Python tentará interpretar a conversão, mas ocasionará um erro pois o tipo é diferente.

~~~python 
preco = "python"

print(float(preco))
>>> 
Traceback (most recent call last):
    File "main.py", line 3, in <module>
        print(float(preco))
ValueError: could not convert string to float: 'python'
~~~

## Funções de Entrada e Saída

- Como solicitar valores para o usuário?

Utilizamos a função built-in `input`, que recebe o dado digitado como string (`str`), ou seja, lê o valor, converte e retorna o valor. 

~~~python 
nome = input("Informe seu nome: ")
>>> Informe seu nome: 
~~~

- Para exibir informações?

Usamos a função built-in `print`. Ela recebe um argumento obrigatório do tipo _varargs_ de objetos e 4 argumentos opcionais (_sep_, _end_, _file_ e _flush_). Todos os objetos são convertidos para _string_, separados por _sep_ e terminados por _end_. A string final é exibida ao usuário.

~~~python 
nome = "Gabriel"
sobrenome = "Antonini"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")

>>> Gabriel Antonini
>>> Gabriel Antonini...
>>> Gabriel#Antonini
~~~
