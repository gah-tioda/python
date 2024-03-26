conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 2500
cheque_especial = 450

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