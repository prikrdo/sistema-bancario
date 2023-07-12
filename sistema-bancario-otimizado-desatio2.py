
def menu():
    menu = '''
    ============ BANCO PR S.A ============
       Bem vindo, digite a opção que 
       deseja realizar:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Listar Usuários
    [6] Nova Conta
    [7] Listar Contas
    [8] Sair

    =====================================
    => '''
    return input(menu)

def depositar(saldo, valor, extrato, /): 
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print(f"\nO valor de R$ {valor:.2f} foi depositado com sucesso!\n")
    else:
        print("!!! Operação falhou: O valor informado é invalido. !!!")

    return saldo, extrato 


def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    saldo_insuficiente = valor > saldo

    limite_excedido = valor > limite

    qtd_saques_excedido = numero_saques >= limite_saques   

    if saldo_insuficiente:
        print("!!! Operação falhou: Você não tem saldo suficiente. !!!")
        print(f"\nSeu saldo é de: R$ {saldo:.2f} ")

    elif limite_excedido:
        print("!!! Operação falhou: O valor do saque excede o limite. !!!")
        print(f"\nO seu limite de saque por operação é de: R$ {limite}")

    elif qtd_saques_excedido:
        print("!!! Operação falhou: Número maximo de saque excedido. !!!")
        print(f"\nVocê ja realizou {numero_saques} saques, seu limite é de {limite_saques} saques.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nO valor de R$ {valor:.2f} foi retirado com sucesso!\n")

    else:
        print("!!! Operação falhou: O valor informado é inválido. !!!")

    return saldo, extrato, numero_saques #Sugestão


def exibir_extrato(saldo,/,*,extrato):
    print("\n===================== EXTRATO =====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===================================================")


def criar_usuario(usuarios):
    cpf = input("Informe o numero do CPF (Somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome do usuário: ")
    data_de_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    nome = nome.upper()
    endereco = endereco.upper()

    usuarios.append({"cpf": cpf, "nome": nome, "data_de_nascimento": data_de_nascimento, "endereco": endereco }) 

    print("\nUsuário criado com sucesso!!!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_usuarios(usuarios):
    if not usuarios: 
        print("Não exite nenhum usuário cadastrado no sistema." )

    else:
        for cliente in usuarios:
                linha=f'''
                    ================ USUARIO ================

                    "CPF"= {cliente['cpf']}
                    "NOME"= {cliente['nome']}
                    "DN"= {cliente['data_de_nascimento']}
                    "ENDERECO"= {cliente['endereco']}

                    =========================================
                '''
                print(linha)


def listar_contas(contas):
    if not contas:
        print("Não exite nenhuma conta cadastrada no sistema.")

    else:
        for conta in contas:
                linha = f'''
                    ================= CONTAS =================

                    "Agência": {conta['agencia']}
                    "C/C": {conta['nro_conta']}
                    "Titular": {conta['usuario']['nome']}

                    =========================================
                '''
                print("Não exite nenhuma conta cadastrada no sistema." if not linha else linha)
                print(linha)



def criar_conta(agencia, nro_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "nro_conta": nro_conta, "usuario": usuario}
    
    else:
        print("\n!!! Usuário não encontrado, fluxo de criação de conta encerrado! !!! ")


def geral():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while 1 == 1:
        opcao_menu =  menu()

        if opcao_menu == "1": #Deposito
            valor = float(input("Digite o valor do deposito: "))

            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao_menu == "2": #Saque
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar( #sugestão
                saldo = saldo,
                valor = valor,
                limite = limite, 
                extrato = extrato, 
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )


        elif opcao_menu == "3": #Extrato
            exibir_extrato(saldo, extrato = extrato)
            print(numero_saques)

            
        elif opcao_menu == "4": #Novo Usuario
            criar_usuario(usuarios)


        elif opcao_menu == "5": #Listar Usuarios
            listar_usuarios(usuarios)


        elif opcao_menu == "6": #Nova Conta 
            nro_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, nro_conta, usuarios)

            if conta:
                contas.append(conta)


        elif opcao_menu == "7": #Listar Contas
            listar_contas(contas)


        elif opcao_menu == "8": # Sair do Sistema
            print('''\nO BANCO PR S.A agradece por utilizar nossos serviços.
                Tenha um bom dia!\n''')
            break


        else:
         print("!!! Operação inválida, por favor selecione novamente a operação desejada. !!!")


geral()





