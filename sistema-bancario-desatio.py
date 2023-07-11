menu = '''
============ BANCO PR S.A ============
   Bem vindo, digite a opção que 
   deseja realizar:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=====================================
=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while 1 == 1:

    opcao_menu = input(menu)

    if opcao_menu == "1":
        valor = float(input("Digite o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"\nO valor de R$ {valor:.2f} foi depositado com sucesso!\n")

        else:
            print("Operação falhou: O valor informado é invalido.")

    elif opcao_menu == "2":
        valor = float(input("Informe o valor do saque: "))

        saldo_insuficiente = valor > saldo

        limite_excedido = valor > limite

        qtd_saques_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Operação falhou: Você não tem saldo suficiente.")
            print(f"\nSeu saldo é de: R$ {saldo:.2f} ")

        elif limite_excedido:
            print("Operação falhou: O valor do saque excede o limite.")
            print(f"\nO seu limite de saque por operação é de: R$ {limite}")

        elif qtd_saques_excedido:
            print("Operação falhou: Número maximo de saque excedido.")
            print(f"\nVocê ja realizou {numero_saques} saques, seu limite é de {LIMITE_SAQUES} saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nO valor de R$ {valor:.2f} foi retirado com sucesso!\n")

        else:
            print("Operação falhou: O valor informado é inválido.")

    elif opcao_menu == "3":
        print("\n===================== EXTRATO =====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================")


    elif opcao_menu == "4":
        print('''\nO BANCO PR S.A agradece por utilizar nossos serviços.
              Tenha um bom dia!\n''')
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")