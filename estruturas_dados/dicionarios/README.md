# Dicionários

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

`{}.clear`

Limpa um dicionário.

~~~python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.clear()
contatos # {}
~~~

`{}.copy`

Cria uma cópia do dicionário. Se alterarmos o original, a cópia não é afetada.

~~~python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"] # {"nome": "Guilherme", "telefone": "3333-
2221"}
copia["guilherme@gmail.com"] # {"nome": "Gui"}
~~~

`{}.fromkeys`

Este método permite criar ou alterar um dicionário com novas chaves somente com o nome das chaves e os valores vazios, ou com valores padrões dentro de cada chave.

Basta passarmos uma lista com todos os valores de chave. 

~~~python
dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": vazio, "telefone": vazio}
~~~

`{}.get`

Outro método para acessar elementos dentro de um dicionário. Diferente de usar o slice, que apresenta `KeyError` quando não encontra uma chave, o `get` possui uma algumas funcionalidades para retornar mensagens personalizadas ao não encontrar a chave.

~~~python
contatos = {
    "gabriel@gmail.com" : {"nome": "Gabriel", "telefone": "3333-1234"}
}

contatos["chave"] # Apresentará KeyError

print(contatos.get("chave")) # retorna None
print(contatos.get("chave", "Chave não encontrada")) #retorna Chave não encontrada
print(contatos.get("gabriel@gmail.com", "Chave não encontrada")) #retorna {'nome': 'Gabriel', 'telefone': '3333-1234'}
~~~

`{}.items`

Retorna os dados do dicionário em formato de lista com tuplas. Muito útil para usar com o `for` e iterar sobre esses valores.

~~~python
contatos = {
    "gabriel@gmail.com" : {"nome": "Gabriel", "telefone": "3333-1234"}
}

print(contatos.items()) # retorna dict_items([('gabriel@gmail.com', {'nome': 'Gabriel', 'telefone': '3333-1234'})])
~~~

`{}.keys`

Retorna as chaves do dicionário em formato de listas. Muito útil para saber quais as chaves do dicionário.

~~~python
contatos = {
    "gabriel@gmail.com" : {"nome": "Gabriel", "telefone": "3333-1234"}
}

print(contatos.keys()) # retorna dict_keys(['gabriel@gmail.com'])
~~~

`{}.pop`

Remove um valor do dicionário baseado na chave que dermos como argumento. Quando encontrado, ele retorna todos os dados dessa chave. Caso não encontrado, podemos colocar como segundo argumento uma mensagem.

~~~python
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.pop("guilherme@gmail.com") # {'nome': 'Guilherme', 'telefone': '3333-2221'}
contatos.pop("guilherme@gmail.com", "Não encontrado") # Não encontrado
~~~

`{}.popitem`

Remove os itens do dicionário conforme sequência. Não é necessário passar argumento. Se não tiver mais itens, ele retorna `KeyError`.

~~~python
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.popitem() # {'nome': 'Guilherme', 'telefone': '3333-2221'}
contatos.popitem() # KeyError
~~~

`{}.setdefault`

Recurso muito útil no dia a dia. Ele verifica se existe a chave no dicionário, se não existir, inclui a nova chave + valor que definirmos no segundo argumento. Caso exista, ele retorna o item e não faz nenhuma modificação.

~~~python
contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna") # "Guilherme"
contato # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28) # 28
contato # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
~~~

`{}.update`

Permite atualizarmos um dicionário. Caso os dados inseridos como argumento seja uma chave + valor inexistente, será criado um novo item; caso contrário, e seja uma chave existente, o valor contido dentro da chave será atualizado.

~~~python
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
contatos # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
~~~

`{}.values`

Este método só retorna os valores contidos em cada chave do dicionário em formato de lista. Muito útil quando não precisamos saber as chaves e só precisamos iterar sobre todos os valores do dicionário.

~~~python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.values() # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])
~~~

`in`

Melhor método para checar se existe uma determinada chave dentro do dicionário. Retorna um valor booleano.

~~~python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

"guilherme@gmail.com" in contatos # True
"megui@gmail.com" in contatos # False
"idade" in contatos["guilherme@gmail.com"] # False
"telefone" in contatos["giovanna@gmail.com"] # True
~~~

`del`

Outra forma de remover um valor de um dicionário. Passamos para o método o objeto que queremos remover.

Se passarmos apenas o nome do dicionário, apaga ele inteiro.

~~~python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"] # remove só o telefone da chave
del contatos["chappie@gmail.com"] # remove todo o conteúdo relacionado à chave

contatos # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome':'Melaine', 'telefone': '3333-7766'}}
~~~