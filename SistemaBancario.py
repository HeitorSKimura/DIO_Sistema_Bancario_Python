import math

def truncateNum(number, dec_plc):
    return math.floor(number * 10 ** dec_plc) / 10 ** dec_plc

def depositar(saldo, valor, extrato, /):
    if(valor < 0):
        print("\nValor não aceitavel, tente novamente.\n")
        return
    else:
        saldo += valor
        extrato += f"Deposito: R$ {truncateNum(valor,2)}\n"
        print("Deposito efetuado com sucesso!!")
        return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numeroSaque, limiteSaque):
    if(numeroSaque != limiteSaque):
        if(valor <= saldo):
            if(valor <= limite):
                numeroSaque += 1
                saldo -= valor
                extrato += f"Saque: R$ {truncateNum(valor,2)}\n"
                print("Saque efetuado com sucesso!!")
            else:
                print("Limite por saque é de R$ 500,00! Tente Novamente.")
        else:
            print("Valor excede o valor total da conta!, tente novamente.\n")
    else:
        print("Saques diário excedido, tente novamente amanhã.")
    return saldo, extrato

def extratoBancario(saldo, /, *, extrato):
    if(saldo == 0 and extrato == ""):
        print("Não foram realizadas movimentações")
        return
    else:
        print(extrato)
        print(f"Saldo Atual: {saldo}")
        return 

def criarUsuario(listaUsuario):
    nome = input("Informe seu nome: ")
    dataNascimento = input("Informe sua data de nascimento(dia/mes/ano): ")
    cpf = input("Informe seu CPF: ")
    usuarioExiste = procurarUsuario(listaUsuario, cpf)
    if usuarioExiste:
        print(f"Usuario com o CPF: {cpf} já existe, Tente novamente.")
        return
    endereco = criarEndereco()

    listaUsuario.append({"nome":nome, "dataNascimento":dataNascimento, "cpf":cpf, "endereco":endereco})
    print(" Usuario Criado com Sucesso ")    

def criarConta(listaConta,listaUsuario):
    cpf = input("Informe o cpf do usuario: ")
    agencia = "0001"
    numero = len(listaConta) + 1
    usuario = procurarUsuario(listaUsuario, cpf)
    if not usuario:
        print(" Usuario não Encontrado! ".center(35,"#"))
        return
    
    listaConta.append({"agencia":agencia, "numero":numero, "usuario":usuario})
    print(" Conta Criado com Sucesso ")

def procurarUsuario(listaUsuario, cpf):
    usuarioAchado = [usuario for usuario in listaUsuario if usuario["cpf"] == cpf]
    return usuarioAchado[0] if usuarioAchado else None

def criarEndereco():
    print("Informe seu Endereco(logradouro - numero - bairro - cidade - estado):")
    logradouro = input("Logradouro: ")
    numero = input("Numero: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado(sigla): ")
    endereco = {"logradouro":logradouro, "numero":numero, "bairro":bairro, "cidade":cidade, "estado":estado}
    return endereco

def mostrarUsuarios(listaUsuario):
    for usuario in listaUsuario:
        print(f'\nNome: {usuario["nome"]} / Cpf: {usuario["cpf"]}')

def mostrarContas(listaConta):
    for conta in listaConta:
        print(f'ID: {conta["numero"]} / Cpf: {conta["usuario"]["cpf"]} / Agencia: {conta["agencia"]}')

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuario
[nc] Nova Conta
[lu] Lista de Usuarios
[lc] Lista de Contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_Usuario = []
lista_Conta = []


while True:

    opcao = input(menu.lower())

    if(opcao == "d"):
        print(" Depositar ".center(26,"-"))
        valor = float(input("Informe o valor para Deposito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif(opcao == "s"):
        print(" Sacar ".center(26,"-"))
        valor = float(input("Informe o valor para Saque: "))
        saldo, extrato = sacar(
            saldo= saldo,
            valor= valor,
            extrato= extrato,
            limite= limite,
            numeroSaque= numero_saques,
            limiteSaque= LIMITE_SAQUES
            )
    elif(opcao == "e"):
        print(" Extrato ".center(26,"#"))
        extratoBancario(saldo, extrato= extrato)
        print("".center(26,"-"))
    elif(opcao == "nu"):
        print(" Novo Usuario ".center(26,"#"))
        criarUsuario(lista_Usuario)
    elif(opcao == "nc"):
        print(" Nova Conta ".center(26,"#"))
        criarConta(lista_Conta, lista_Usuario)
    elif(opcao == "lu"):
        print(" Lista de Usuarios ".center(26,"#"))
        mostrarUsuarios(lista_Usuario)
    elif(opcao == "lc"):
        print(" Lista de Contas ".center(26,"#"))
        mostrarContas(lista_Conta)
    elif(opcao == "q"):
        print("Sistema Encerrado".center(26,"*"))
        break
    else:
        print("Opção Inválida, por favor insira novamente a operação desejada.")