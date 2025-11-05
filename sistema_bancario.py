import re

usuarios = []
contas = []

LIMITE = 500
LIMITE_SAQUES = 3

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor de saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def extrato(saldo, /, *, extrato):
    print("\n------------------- Extrato -------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("-----------------------------------------------")

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    cpf = re.sub(r'\D', '', cpf)  # Remove non-numeric characters
    if any(u['cpf'] == cpf for u in usuarios):
        print("CPF já cadastrado!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro - nro - bairro - cidade/sigla estado): ")
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def criar_conta_corrente():
    cpf = input("Informe o CPF do usuário: ")
    cpf = re.sub(r'\D', '', cpf)
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado!")
        return
    numero_conta = len(contas) + 1
    contas.append({
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    })
    print(f"Conta criada com sucesso! Agência: 0001, Conta: {numero_conta}")

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")

saldo = 0
extrato = ""
numero_saques = 0

while True:
    print("\nMenu:")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[u] Criar Usuário")
    print("[c] Criar Conta Corrente")
    print("[l] Listar Contas")
    print("[x] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo, valor=valor, extrato=extrato,
            limite=LIMITE, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        extrato(saldo, extrato=extrato)

    elif opcao == "u":
        criar_usuario()

    elif opcao == "c":
        criar_conta_corrente()

    elif opcao == "l":
        listar_contas()

    elif opcao == "x":
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
