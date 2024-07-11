def menu():
    menu = """\n
    =====================MENU=====================

    [0]\tDepositar
    [1]\tSacar
    [2]\tExtrato
    [3]\tNovo Usuário
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tSair 

    =>"""
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado:\tR$ {valor:.2f}\n"
        print("\n= Depósito Realizado com sucesso! =")

    else:
        print("\n= Depósito não realizado. Por favor, informe um valor válido para o depósito. =")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if valor > 0:
        if excedeu_saldo:
            print("\n= Operação não realizada. Saldo indisponível para o saque. =")
            
        elif excedeu_limite:
            print("\n= O valor do saque excede o valor limite para saques em sua conta. Por favor, tente novamente. =")

        elif excedeu_saques:
            print("\n= Você já realizou o número máximo de saques na data de hoje. =")

        else:
            saldo -= valor
            extrato += f"Saque realizado:\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\n= Saque realizado com sucesso! =")

    else:
            print("\n= Operação não realizada. Valor inválido para saque. =")
                
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
        
        print("\n================ EXTRATO ================")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\n= Seu saldo disponível no momento é: R$ {saldo:.2f} =\n")
        print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF (utilize apenas números): ")
    usuario = filtrar_usuario(usuarios, cpf)

    if usuario:
        print("Já existe um usuário cadastrado com este número de CPF.")
        
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço completo (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("\n= Parabéns! Usuário criado com sucesso. =")

def filtrar_usuario(usuarios, cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF (utilize apenas números): ")
    usuario = filtrar_usuario(usuarios, cpf)

    if usuario:
        print("\n= Parabéns! Sua conta foi criada com sucesso. =")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    else:
        print("CPF não encontrado no sistema, por favor, crie um usuário antes de tentar abrir uma conta.")

def listar_contas(contas):
    for conta in contas:
        dados_conta = f'''
            Agência:\t{conta['agencia']}
            Número de Conta:\t{conta['numero_conta']}
            Nome do Titular:\t{conta['usuario']['nome']}
'''
        print(dados_conta)
        print("=" * 50)

def main():
    agencia = "0001"
    limite_saques = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opçao = int(menu())

        if opçao==0:
            print("=== Realizar Depósito ===\n\n\n\n")
            valor = float(input("Por favor, informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opçao==1:
            print("=== Realizar Saque ===\n\n\n\n")
            valor = float(input("Por favor, informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = limite_saques,
            )

        elif opçao==2:
            exibir_extrato(saldo, extrato = extrato)

        elif opçao==3:
            criar_usuario(usuarios)

        elif opçao==4:
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opçao==5:
            listar_contas(contas)

        elif opçao==6:
            print("Muito obrigado por utilizar nossos serviços!")
            break

        else:
            print("Operação inválida. Por favor, selecione um valor válido no menu de opções.")

main()