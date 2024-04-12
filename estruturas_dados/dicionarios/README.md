# Dicionarios

Conjunto não ordenado de pares (chave:valor), onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves (`{}`) e contém uma lista de pares (chave:valor) separados por vírgulas.

As chaves precisam ser valores imutáveis, como uma tupla ou strings. Já o valor, pode ser qualquer tipo de objeto, tanto imutável quanto mutável.

Os dicionários não permitem chaves com valores repetidos.

~~~python
pessoa = {"nome": "Gabriel", "idade": 24}

pessoa = dict(nome="Gabriel", idade=24)

pessoa["telefone"] = "3333-1234" # {"nome": "Gabriel", "idade": 24, "telefone": "3333-1234"}
~~~

### _Acesso e atualização dos dados_

Para acessar, colocamos o nome da chave dentro dos colchetes. Sem o sinal de atribuição do exemplo anterior, o Python entende que estamos querendo acessar o conteúdo e não atribuir.

~~~python
dados = {"nome": "Gabriel", "idade": 24, "telefone": "3333-1234"}

dados["nome"] # "Gabriel"
dados["idade"] # 24 
dados["telefone"] # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 19 
dados["telefone"] = "9999-2727"

dados # {"nome": "Maria", "idade": 19, "telefone": "9999-2727"}
~~~

### _Dicionários aninhados_

Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável (strings e números).

~~~python
contatos = {
    "gabriel@gmail.com" : {"nome": "Gabriel", "telefone": "3333-1234"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3556-2020"},
}

dados["gabriel@gmail.com"]["telefone"] # acessando o dado do telefone "3333-1234"
~~~

### _Iterar dados_

Podemos acessar os valores de um dicionário através da iteração com um `for`.

~~~python
contatos = {
    "gabriel@gmail.com" : {"nome": "Gabriel", "telefone": "3333-1234"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3556-2020"},
}

for chave in contatos:
    print(chave, contatos[chave])

#melhor forma de acessar e iterar:

for chave, valor in contatos.items():
    print(chave, valor)

# gabriel@gmail.com {'nome': 'Gabriel', 'telefone': '3333-1234'}
# giovana@gmail.com {'nome': 'Giovana', 'telefone': '3556-2020'}
~~~

### _Métodos da classe_ `dict`