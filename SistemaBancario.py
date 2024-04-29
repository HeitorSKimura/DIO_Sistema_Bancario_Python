import math

def truncateNum(number, dec_plc):
    return math.floor(number * 10 ** dec_plc) / 10 ** dec_plc

def saque():
    return

def depositar():
    return

def extrato():
    return

def criarUsuario(listaUsuario):
    nome = input("Informe seu nome: ")
    dataNascimento = input("Informe sua data de nascimento(dia/mes/ano): ")
    cpf = input("Informe seu CPF: ")
    endereco = criarEndereco()
    for i in listaUsuario:
        if(i == cpf):
            return "Conta Existente! Tente novamente."
        else:
            listaUsuario.append(nome, dataNascimento, cpf, endereco)
    

def criarConta():
    return

def criarEndereco():
    print("Informe seu Endereco(logradouro - numero - bairro - cidade - estado):")
    logradouro = input("Logradouro: ")
    numero = input("Numero: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado(sigla): ")
    endereco = {"endereco" : {"logradouro":logradouro, "numero":numero, "bairro":bairro, "cidade":cidade, "estado":estado} }
    return endereco

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
lista_Usuario = []
lista_Conta = []

criarUsuario(lista_Usuario)

print(lista_Usuario[0])
# while True:

#     opcao = input(menu.lower())

#     if(opcao == "d"):
#         print(" Depositar ".center(26,"-"))
#         while(True):
#             valor = float(input("Informe o valor que deseja Depositar: "))
#             if(valor < 0):
#                 print("\nValor não aceitavel, tente novamente.\n")
#                 continue
#             else:
#                 saldo += valor
#                 extrato += f"Deposito: R$ {truncateNum(valor,2)}\n"
#                 break
#     elif(opcao == "s"):
#         print(" Sacar ".center(26,"-"))
#         while(True):
#             if(numero_saques != LIMITE_SAQUES):
#                 if(saldo != 0):
#                     valor = float(input("Informe o valor que deseja Sacar: "))
#                     if(valor <= 500):            
#                         if(valor <= saldo):
#                             extrato += f"Saque: R$ {truncateNum(valor,2)}\n"
#                             numero_saques += 1
#                             saldo -= valor
#                             break
#                         else:
#                             print("Valor excede o valor total da conta!, tente novamente.\n")
#                     else:
#                         print("Valor maximo por saque é de R$ 500.00, tente novamente.")
#                 else:
#                     print("Não será possiver sacar o dinheiro por falta de saldo.")
#                     break
#             else:
#                 print("Saques diário excedido, tente novamente amanhã.")
#                 break
#     elif(opcao == "e"):
#         print(" Extrato ".center(26,"#"))
#         if(extrato == ""):
#             print("Não foram realizadas movimentações")
#         print(extrato)        
#         print(f"Saldo Atual: {saldo}")
#         print("".center(26,"-"))
#     elif(opcao == "q"):
#         print("Sistema Encerrado".center(26,"*"))
#         break
#     else:
#         print("Opção Inválida, por favor insira novamente a operação desejada.")