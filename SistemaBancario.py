import math

def truncateNum(number, dec_plc):
    return math.floor(number * 10 ** dec_plc) / 10 ** dec_plc

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
        print(" Depositar ".center(26,"-"))
        while(True):
            valor = float(input("Informe o valor que deseja Depositar: "))
            if(valor < 0):
                print("\nValor não aceitavel, tente novamente.\n")
                continue
            else:
                saldo += valor
                extrato += f"Deposito: R$ {truncateNum(valor,2)}\n"
                break
    elif(opcao == "s"):
        print(" Sacar ".center(26,"-"))
        while(True):
            if(numero_saques <= LIMITE_SAQUES):
                valor = float(input("Informe o valor que deseja Sacar: "))
                if()
    elif(opcao == "e"):
        print(" Extrato ".center(26,"#"))
        print(extrato)
    elif(opcao == "q"):
        print("Sistema Encerrado")
        break
    else:
        print("Opção Inválida, por favor insira novamente a operação desejada.")