# Conjuntos - Estrutura de dados `set`

Um `set` é uma coleção (`collection`) que **não possui** objetos repetidos. Usamos para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

Exemplo: se temos uma lista com vários elementos duplicados e queremos removê-lo, basta passarmos o construtor `set` com a lista dentro que ele retorna sem duplicidade.

O `set` espera um objeto iterável e ele não retorna um valor ordenado corretamente.

~~~python
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}
~~~

### _Acessando os dados_

Conjuntos em Python **não suportam indexação** e nem **fatiamento**. Caso queira acessar os seus valores é necessário converter o conjunto para lista. 

~~~python
numeros = {1, 2, 3, 4}

numeros = list(numeros)

print(numeros[0]) # 1
~~~

### _Iterar conjuntos_

A forma mais comum para percorrer os dados de um conjunto é utilizando o `for`.

~~~python
carros = {"gol", "prisma", "celta"}

for carro in carros:
    print(carro)
~~~

### _Função_ `enumerate`

As vezes é necessário saber qual o índice do objeto dentro do laço `for`. Para isso usamos o `enumerate`.

~~~python
carros = {"gol", "prisma", "celta"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
~~~

### _Métodos da classe_ `set`

Todas as operações matemáticas que são realizadas com conjuntos podem ser feitas com o `set` em Python.

`{}.union`

Junta todos os elementos.

![alt text](image-5.png)

~~~python
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}
~~~

`{}.intersection`

Retorna os valores que se conectam, que são iguais entre os dois conjuntos. 

![alt text](image-4.png)

~~~python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.union(conjunto_b) # {2, 3}
~~~

`{}.difference`

Retorna o valor diferente que tem no conjunto A em relação ao B e vice-versa.

![alt text](image-3.png)

~~~python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}
~~~

`{}.symmetric_difference`

Retorna os valores diferentes da intersecção, valores que são divergentes entre os dois conjuntos.

![alt text](image-2.png)

~~~python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}
~~~

`{}.issubset`

Retorna um valor booleano comparando se os valores de conjunto A estão contidos no B e vice-versa.

![alt text](image-1.png)

~~~python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False
~~~

`{}.issuperset`

"O contrário do subset", ele verifica se todos os elementos de B estão contidos em A. Ou seja, um superconjunto de A.

![alt text](image-6.png)

~~~python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True
~~~

`{}.isdisjoint`

Operação de conjunto disjunto, ou seja, são conjuntos que não se juntam/se conectam/possui intersecção. 

![alt text](image-7.png)

~~~python
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True - são totalmente diferentes
conjunto_b.isdisjoint(conjunto_c) # False - se conectam através do 1
~~~

`{}.add`

Adiciona um elemento ao conjunto, **se já não houver**.

~~~python
sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}
~~~

`{}.clear`

Limpa o conjunto todo.

~~~python
sorteio = {1, 23}

sorteio # {1, 23}
sorteio.clear() # {}
sorteio # {}
~~~

`{}.copy`

Cria uma cópia do conjunto. Caso seja modificado a variável principal a cópia não é alterada. 

~~~python
sorteio = {1, 23}

sorteio # {1, 23}
sorteio.copy()
sorteio # {1, 23}
~~~

`{}.discard`

Remove os valores que existirem dentro do conjunto e, caso não exista, não fará nenhuma alteração.

~~~python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}
~~~

`{}.pop`

Remove os elementos conforme a sequência da pilha, possui o comportamento de começar pela esquerda para direita (do começo da sequência para o fim)

~~~python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.discard() # 0
numeros.discard() # 1
numeros # {2, 3, 4, 5, 6, 7, 8, 9}
~~~

`{}.remove`

Mesmo comportamento do `discard`, contudo, caso o elemento inserido como argumento não existir no conjunto, a execução resultará em **erro**, enquanto o `discard` continua executando normalmente e não faz nenhuma alteração.

~~~python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.remove(0) # 0
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}
~~~

`len`

Retorna o tamanho do conjunto.

~~~python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

len(numeros) # 10 - pois ele só contabiliza os valores únicos e remove os duplicados.
~~~

`in`

Serve para verificarmos um valor dentro de um conjunto, retorna um booleano.

~~~python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros # True
10 in numeros # False
~~~