contatos = {
    "gabriel@gmail.com" : {"nome": "Gabriel", "telefone": "3333-1234"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3556-2020"},
}

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)