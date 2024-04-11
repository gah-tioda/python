# Listas

Listas em Python armazenam qualquer tipo de objeto (qualquer tipo de dado, diferente de outras linguagens que é preciso declarar qual tipo de dados será armazenado na lista) de maneira sequencial. Eles são objetos mutáveis, ou seja, podem ser alterados após a criação.

Para criar listas podemos:

- Utilizando a função/construtor `list`;
- Função `range`;
- Colocando valores separado por vírgula dentro de colchetes `[o,1,2,3]`

Exemplo:

~~~python
frutas = ['laranja', 'maçã', 'uva']

frutas[]

letras = list("python") #neste caso a lista será criada dividindo cada letra em elementos da lista.

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
~~~

### _Acesso direto_

A lista é uma sequência, portando, podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero.

~~~python
frutas = ['laranja', 'maçã', 'uva', 'pêra']

frutas[0] #laranja
frutas[1] #maçã
~~~

### _Índices negativos_

Sequências suportam indexação negativa. A contagem começa em -1. Ele começa a contar o último item da lista.

~~~python
frutas = ['laranja', 'maçã', 'uva', 'pêra']

frutas[-1] #pêra
frutas[-3] #maçã
~~~

### _Listas aninhadas_

A lista é um objeto e uma estrutura de dados que armazena todos os outros tipos de objetos Python, inclusive outras listas. Com isso, criamos estruturas bidimensionais (matriz bidimensional, tabelas), e acessar informando os índices de linha e coluna. Chamamos isso também de _listas aninhadas_.

~~~python
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] #[1, "a", 2]
matriz[0][0] #1
matriz[0][-1] #2
matriz[-1][-1] # "c"
~~~

### _Fatiamento_

Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursos deve "pular" no acesso. 

A sintaxe é: [posicao_inicial:posicao_final - 1:quantas_posicoes_pular]

~~~python
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] #["y", "t", "h", "o", "n"] - se passar um inicial e final sem nada, ele pega a partir da posição inicial e o restante da lista toda
lista[:2] #["p", "y"] - a partir da posição final, subtrai uma posição e traz todo o resto
lista[1:3] #["y", "t"] - começa a partir da posição 1 até 2 (3-1)
lista[0:3:2] # ["p", "t"] - começa em 0, pula 2, até o 3-1
lista[::] # vazio retorna toda a lista ["p", "y", "t", "h", "o", "n"]
lista[::-1] # retorna a lista de forma espelhada, ["n", "o", "h", "t", "y", "p"]
~~~

### _Iterar lista_

A forma mais comum para percorrer os dados de uma lista é utilizando o `for`.

~~~python
carros = ["gol", "prisma", "celta"]

for carro in carros:
    print(carro)
~~~

### _Função_ `enumerate`

As vezes é necessário saber qual o índice do objeto dentro do laço `for`. Para isso usamos o `enumerate`.

~~~python
carros = ["gol", "prisma", "celta"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
~~~

### _Compreensão de listas_ `list comprehension`

A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente. Usar esta função é mais performática pelo interpretador do Python.

- Filtro versão 1

~~~python
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0
        pares.append(numero)
~~~

- Filtro versão 2 (usando comprehension)

Sintaxe: primeira parte é o return da função, segunda o for ou parte da iteração, condição ou ação dentro do `for`

~~~python
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
~~~

- Modificando valores versão 1

~~~python
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
        quadrado.append(numero ** 2)
~~~

- Modificando valores versão 2

~~~python
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
~~~

### _Métodos da classe list_

`append`

É um método que adiciona itens à lista. 

~~~python
lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista) #[1, "Python", [40,30,20]]
~~~

`clear`

Usado para limpar uma lista

~~~python
lista = [1, "Python", [40, 30, 20]]

print(lista) #[1, "Python", [40,30,20]]

lista.clear()

print(lista) # []
~~~

`copy`

Utilizado para criar uma cópia da lista. Com ela podemos alterar a lista original sem alterar a cópia e vice-cersa.

~~~python
lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()
~~~

`count`

Conta quantas vezes um determinado valor aparece na lista.

~~~python
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") #1
cores.count("azul") #2
cores.count("verde") #1
~~~

`extend`

Diferente do append, que adicionamos itens de 1 em 1, podemos criar uma outra lista com vários elementos e usar o extend para fazer o merge entre uma existente e a nova. Inclui valores duplicados caso houver.

~~~python
linguagens = ["Python", "JS", "C"]

print(linguagens) # ["Python", "JS", "C"]

linguagens.extend(["Java", "C#"])

print(linguagens) #["Python", "JS", "C", "Java", "C#"]
~~~

`index`

Retorna a posição da primeira ocorrência que ele encontrar do valor em uma lista e não todas as ocorrências. 

~~~python
linguagens = ["Python", "JS", "C", "Java", "C#"]

linguagens.index("Java") #3
linguagens.index("Python") #0
~~~

`pop`

A lista python é criada com o conceito de "pilhas", ou seja, os dados vão sendo colocados em sequência um em cima do outro. O `pop`, por padrão, remove sempre o último item adicionado ao final da lista. Se passarmos o índice do item, ele remove o item.

~~~python
linguagens = ["Python", "JS", "C", "Java", "C#"]

linguagens.pop() # C#
linguagens.pop() # Java
linguagens.pop() #3 C
linguagens.index(0) # Python
~~~

`remove`

Segunda forma de remover objetos da lista. Ao invés do índice, passamos o valor do objeto em si. Ele remove apenas a primeira ocorrência que encontrar. 

~~~python
linguagens = ["Python", "JS", "C", "Java", "C#"]

linguagens.remove("C")

print(linguagens) #["Python", "JS", "Java", "C#"]
~~~