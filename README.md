# 👨🏻‍💻 Desafio [DIO](https://web.dio.me):

## Parte 1
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

1. **💰 Operação de Depósito:**
    - Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

2. **💸 Operação de Saque:**
    - O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

3. **😱 Operação de Extrato:**
    - Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

## Parte 2

### Objetivo Geral:
Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: Cadastrar Usuário (Cliente) e Cadastrar Conta Bancária.

1. **Saque:**
    - A função saque deve receber os argumentos apenas por nome (keyword only). 
        - Sugestão dos argumentos
            - saldo
            - valor
            - extrato
            - limite
            - numeros_saques
            - limite_saque
        - Sugestão de retorno:
            - Saldo
            - Extrato
2. **Depósito:**
    - A função depósito deve receber os argumentos apenas por posição (positional only).
        - Sugestão de argumentos:
            - Saldo
            - Valor
            - Extrato
        - Sugestão de retorno:
            - Saldo
            - Extrato
3. **Extrato:**
    - A função extrato deve receber os argumentos por posição e nome (positional only and keyword only).
        - Argumentos posicionais: **saldo**.
        - Argumentos nomeados: **extrato**
4. **Novas Funções:**
    - Criar Usuário
        - O programa deve armazenar os usuários em uma lista, um usuário e composto por:
            - nome
            - data de nascimento
            - cpf e endereço
        - O Endereço é uma string com o formato:
            - logradouro
            - numero
            - bairro
            - cidade/sigla estado
        - Deve ser armazenado somente os numeros do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.
    - Criar Conta Corrente
        - O programa deve armazenar Contas em uma lista, uma conta é composta por: 
            - agência
            - numero da conta
            - usuário 
        - O Numero da conta é sequencial, iniciando em 1.
        - O numero da agência é fixo: "0001".
        - O Usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.