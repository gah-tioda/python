saldo = 2000.0
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1: 
    valor = float(input("Informe o valor do saque: "))
elif opcao == 2:
    print("Exibindo extrato...")
else:
    print("Opção inválida")