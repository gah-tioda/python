
# Estruturas Condicionais e de Repetição em Python

### _Estética de código_

Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina. 

### _Bloco de comando_

As linguagens de programação costumam utilizar caracteres ou palavras reservadas para determinar o ínicio e fim do bloco. Em Java e C, por exemplo, utilizamos chaves:

~~~java
void sacar(double valor) { //início do bloco do método

    if (this.saldo >= valor) { //início do bloco if
        this.saldo -= valor;
    } // fim do bloco if

} // fim do bloco do método
~~~

Bloco em Java sem formatar:

~~~java
void sacar(double valor) { //início do bloco do método
if (this.saldo >= valor) { //início do bloco if
this.saldo -= valor;
} // fim do bloco if
} // fim do bloco do método
~~~

O código funciona, mas a manutenção e leitura do código neste caso fica díficil.

### _Utilizando espaços_

Em Python, existe uma convenção com boas práticas para escrita do código. No documento, é indicado utilizar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco entre eles.

~~~python
def sacar(self, valor: float) -> None: #Início do bloco do método

    if self.saldo >= valor: # início do bloco if

        self.saldo -= valor
    
    #fim do bloco if

#fim do bloco do método    
~~~

_ISSO NÃO FUNCIONA EM PYTHON!_
~~~python
def sacar(self, valor: float) -> None: #Início do bloco do método
if self.saldo >= valor: # início do bloco if
self.saldo -= valor
#fim do bloco if
#fim do bloco do método
~~~

### _Estruturas Condicionais_

Estruturas Condicionais permitem o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas. Por exemplo, é uma condição que precisa ser satisfeita para realizar uma ação.

- `if`

Uma estrututa condicional simples, composta por um único desvio, pode ser criado com a palavra reservada `if`. O comando testará a expressão lógica e, em caso de retorno verdadeiro, as ações presentes no bloco de código do if serão executadas.

Exemplo:

~~~python
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque: 
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")
~~~

- `if`/`else`

Para criar uma estrutura condicional com dois valores, podemos utilizar as palavras reservadas `if` e `else`. Se a expressão lógica for verdadeira, será executada o bloco de código do if. Caso contrário, será executado o bloco do else.

Exemplo:

~~~python
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque: 
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")
~~~

- `if`/`elif`/`else`

Em alguns casos, queremos mais de dois desvios, para isso, podemos utilizar a palavra reservada `elif`. O elif é composto por uma nova expressão lógica que será testada e, caso retorne verdadeiro, será executado o respectivo bloco de código. Não existe número máximo de elifs que podemos usar, porém, é recomendado não criar grandes estruturas condicionais pois podem aumentar a complexidade do código. 

Exemplo:

~~~python
saldo = 2000.0
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1: 
    valor = float(input("Informe o valor do saque: "))
elif opcao == 2:
    print("Exibindo extrato...")
else:
    print("Opção inválida")
~~~

- `if` aninhado

Podemos criar estruturas condicionais aninhadas, para isso, basta adicionar estruturas if/elif/else dentro do bloco de código destas estruturas.

Exemplo:

~~~python
if conta_normal:
    if saldo >= saque:
        print("Saque realizado")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado")
    else:
        print("Saldo insuficiente!")
else: 
    print("Sistema não reconheceu o tipo, entre em contato com o gerente.")
~~~

- `if` ternário

Este caso permite escrevermos uma condição em uma única linha. Ele é composto por três partes, a primeira é o retorno caso a expressão retorne `verdadeiro`, a segunda é a expressão lógica, e a terceira é o retorno caso a expressão não seja atendida. 

Ideal para validações mais simples, deixando o código mais legível e facilidade na manutenção.

Exemplo:

~~~python
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
~~~

### _Estruturas de repetição_

As estruturas de repetição são utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica. Ou seja, um código pode ser executado quantas vezes definirmos ou até satisfazer uma determinada condição.

- `for`

O comando `for` é usado para percorrer um objeto iterável (string, por exemplo). Faz sentido usar a estrutura quando sabemos o número exato de vezes que nosso bloco de código precisa ser executado. Ou quando queremos percorrer um objeto iterável. 

Exemplo: 

~~~python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() #adiciona uma quebra de linha
~~~

- `for`/`else`

A única diferença é que ao final da execução, ele executará o bloco de código do `else`.

Exemplo:

~~~python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: 
    print() #adiciona uma quebra de linha
    print("Executa no final do laço")
~~~

- Função `range`

Utilizada muito com o `for` para o controle de iterações, é uma função built-in do Python. Ela produz uma sequência de números inteiros a partir de um ínicio (inclusivo - considera na sequência) para um fim (exclusivo - fica fora da sequência). Se usarmos `range(i,j)` será produzido:

i, i+1, i+2, i+3, ..., j-1

Ela recebe três argumentos: stop (obrigatório), start (opcional) e step (opcional - pula de x em x vezes a sequência)

Exemplo com o `for`:

~~~python
for numero in range(0,11):
    print(numero, end=" ")

>>> 0 1 2 3 4 5 6 7 8 9 10

#exibindo a tabuada do 5

for numero in range(0,51,5):
    print(numero, end=" ")

>>> 0 5 10 15 20 25 30 35 40 45 50
~~~

- `while`

Utilizado para repetir um bloco de código várias vezes. Faz sentido usar o while quando não sabemos o número exato de vezes que o bloco de código deve ser executado.

Exemplo:

~~~python
opcao = -1

while opcao != 0:
    opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
~~~

- `while`/`else`

Idêntico ao anterior mas com o else ao final da estrutura. 

Exemplo:

~~~python
opcao = -1

while opcao != 0:
    opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema, até logo!")
~~~

- `break`

Comando que interrompe uma repetição quando utilizamos o `while`. A execução é interrompida quando alguma condição é satisfeita.

Exemplo:

~~~python
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

# É possível usar com for também
    
for numero in range(100):

    if numero == 10:
        break

    print(numero, end=" ")
~~~

- `continue`

Comando para desviarmos de alguma situação específica dentro do laço. Ou seja, ele ignora a condição e continua rodando os outros comandos. 

Exemplo: 

~~~python
#uso do continue, exemplo de programa para apenas exibir números ímpares

for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")

>>> 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99
~~~