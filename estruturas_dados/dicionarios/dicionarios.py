contatos = {
    "gabriel@gmail.com" : {"nome": "Gabriel", "telefone": "3333-1234"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3556-2020"}
}

print(contatos.get("gabriel@gmail.com", "Chave não encontrada"))

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# contatos = {
#     "gabriel@gmail.com" : {"nome": "Gabriel", "telefone": "3333-1234"}
# }

print(contatos.items())

print(contatos.keys())