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