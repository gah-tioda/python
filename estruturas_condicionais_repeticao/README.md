# Estruturas Condicionais e de Repetição em Python

- **Estética de código**

Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina. 

- **Bloco de comando**

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

- **Utilizando espaços**

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