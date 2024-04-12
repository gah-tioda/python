class Pessoa:
    pass #usar o pass evita obter um erro quando criamos algo que não pode ter valores vazios.

p = Pessoa()
if isinstance(p, Pessoa):
    print("O objeto p é uma instância da classe Pessoa.")