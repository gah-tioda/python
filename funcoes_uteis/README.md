# Funções úteis no Python

Criei este documento com o intuito de guardar informações sobre funções úteis no Python

`isinstance(arg1=objeto,arg2=tipo_dado)`

Esta função checa se um determinado objeto, variável, valor faz parte de uma classe ou tipo. É extremamente útil para momentos de validação de dados, tratamento condicional de objetos, verificação de compatibilidade de tipos, etc.

A função também considera subclasses do tipo especificado, exemplo, se uma classe B herda da classe A, um objeto da classe B também será considerada uma instância da classe A. Útil em situações em que queremos verificar se um objeto é de um determinado tipo ou de qualquer uma de suas subclasses.

Exemplos:

- Verificar se um objeto é do tipo específico

~~~python
x = 10
if isinstance(x, int):
    print("A variável x é um inteiro.")
~~~

- Verificar se um objeto é de qualquer um de vários tipos

~~~python
x = 10
if isinstance(x, (int, float)):
    print("A variável x é um inteiro ou um float.")
~~~

- Verificar se um objeto é uma instância de uma classe específica

~~~python
class Pessoa:
    pass

p = Pessoa()
if isinstance(p, Pessoa):
    print("O objeto p é uma instância da classe Pessoa.")
~~~

Mais exemplos em: [Python: Aprenda a usar a função isinstance para verificar tipos de dados](https://awari.com.br/python-aprenda-a-usar-a-funcao-isinstance-para-verificar-tipos-de-dados/?utm_source=blog&utm_campaign=projeto+blog&utm_medium=Python:%20Aprenda%20a%20usar%20a%20fun%C3%A7%C3%A3o%20isinstance%20para%20verificar%20tipos%20de%20dados)

`map()`

Essa função executa uma outra função para cada item em um objeto iterável. Exemplo:

A função map no exemplo abaixo está aplicando o `int` para cada valor recebido no `input`.

~~~python
capacidade_atual, aumento_percentual = map(int, input().split(" "))
~~~

[Python map() Function](https://www.w3schools.com/python/ref_func_map.asp)

`split()`

A função divide uma string em uma lista baseado no separador entre cada elemento informado como parâmetro. No exemplo abaixo usamos um espaço.

~~~python
capacidade_atual, aumento_percentual = map(int, input().split(" "))
~~~

[Python String split() Method](https://www.w3schools.com/python/ref_string_split.asp)