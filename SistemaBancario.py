menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = "Extrato Bancario\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu.lower())

    if(opcao == "d"):
        valor = float(input("Informe o valor que deseja depositar: "))
        while(valor < 0):
            print("Valor não permitido, tente novamente")
            valor = float(input("Informe o valor que deseja depositar: "))
        saldo += valor
        extrato += f"{saldo}"
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