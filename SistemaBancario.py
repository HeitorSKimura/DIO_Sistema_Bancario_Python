menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = "Extrato Bancário:\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu.lower())

    if(opcao == "d"):
        print("Depositar:")
        while(True):
            valor = float(input("Informe o valor que deseja Depositar: "))
            if(valor < 0):
                print("Valor não aceitavel, tente novamente.")
                continue
            else:
                saldo += valor
                extrato += f"Deposito: R$ {valor}\n"
                break
    elif(opcao == "s"):
        print("Sacar:")
    elif(opcao == "e"):
        print("Extrato:")

    elif(opcao == "q"):
        print("Sistema Encerrado")
        break
    else:
        print("Opção Inválida, por favor insira novamente a operação desejada.")