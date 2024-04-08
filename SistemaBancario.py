menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu.lower())

    if(opcao == "d"):
        print("Depositar")
    elif(opcao == "s"):
        print("Sacar")
    elif(opcao == "e"):
        print("Extrato")
    elif(opcao == "q"):
        print("Sistema Encerrado")
        break
    else:
        print("Opção Inválida, por favor insira novamente a operação desejada.")