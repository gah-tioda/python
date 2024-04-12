# Tuplas

As Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que as tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe **tuple**, ou colocando valores separados por vírgula de parênteses.

Uma boa prática é colocar uma vírgula ao final do elemento dentro da tupla, pois isso garante que o interpretador não confunda a tupla com uma precedência de operadores matemáticos.

~~~python
frutas = ('laranja', 'maçã', 'uva',)

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ("Brasil",)
~~~

### _Acesso direto_

A tupla é uma sequência, portanto, podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero.

~~~python
frutas = ('laranja', 'maçã', 'uva',)

frutas[0]
frutas[1]
~~~

- Índices negativos

~~~python
frutas = ('laranja', 'maçã', 'uva',)

frutas[-1]
frutas[-3]
~~~

### _Tuplas aninhadas_

As tuplas também podem armazenar todos os tipos de objetos Python, inclusive outras tuplas. Podemos criar estruturas bidimensionais (tabelas) a acessar com índice de linha e coluna.

~~~python
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0] #(1, "a", 2)
matriz[0][0] #1
matriz[0][-1] #2
matriz[-1][-1] # "c"
~~~

### _Fatiamento_

Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursos deve "pular" no acesso. 

A sintaxe é: [posicao_inicial:posicao_final - 1:quantas_posicoes_pular]

~~~python
tupla = ("p", "y", "t", "h", "o", "n")

tupla[2:] #["y", "t", "h", "o", "n"] - se passar um inicial e final sem nada, ele pega a partir da posição inicial e o restante da lista toda
tupla[:2] #["p", "y"] - a partir da posição final, subtrai uma posição e traz todo o resto
tupla[1:3] #["y", "t"] - começa a partir da posição 1 até 2 (3-1)
tupla[0:3:2] # ["p", "t"] - começa em 0, pula 2, até o 3-1
tupla[::] # vazio retorna toda a lista ["p", "y", "t", "h", "o", "n"]
tupla[::-1] # retorna a lista de forma espelhada, ["n", "o", "h", "t", "y", "p"]
~~~

### _Iterar tupla_

A forma mais comum para percorrer os dados de uma tupla é utilizando o `for`.

~~~python
carros = ("gol", "prisma", "celta",)

for carro in carros:
    print(carro)
~~~

### _Função_ `enumerate`

As vezes é necessário saber qual o índice do objeto dentro do laço `for`. Para isso usamos o `enumerate`.

~~~python
carros = ("gol", "prisma", "celta",)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
~~~

### _Métodos da classe tuple_

`count`

Conta quantas vezes um determinado valor aparece na tupla.

~~~python
cores = ("vermelho", "azul", "verde", "azul",)

cores.count("vermelho") #1
cores.count("azul") #2
cores.count("verde") #1
~~~

`index`

Retorna a posição da primeira ocorrência que ele encontrar do valor em uma tupla e não todas as ocorrências. 

~~~python
linguagens = ("Python", "JS", "C", "Java", "C#",)

linguagens.index("Java") #3
linguagens.index("Python") #0
~~~

`len`

Ele informa o tamanho dos objetos.

~~~python
linguagens = ("Python", "JS", "C", "Java", "Csharp",)

linguagens.len() # 5 é o tamanho da lista
~~~