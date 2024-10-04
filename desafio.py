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
    opcao = input(menu)

    if opcao == 'd':
        print("Depósito")

        valor_deposito = float(input("Digite o valor do depósito: "))

        if(valor_deposito > 0):
            # print("Depósito realizado com sucesso !")
            saldo += valor_deposito
            # print(saldo)
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print("Valor de depósito incorreto !")


    elif opcao == 's':
        print("Saque")
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        # valor_saque = (valor_saque)

        if(valor_saque <= 0):
            print("Valor de saque incorreto!")

        elif(valor_saque > 500):
            print("Seu limite de saque é de R$ 500")

        else:
            numero_saques += 1

            if (numero_saques > LIMITE_SAQUES):
                print("Limite diário de saques atingido!")


            else:
                print("Saque realizado com sucesso! ")
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"

    elif opcao == 'e':
        print("Extrato")
        print(f"""
        EXTRATO BANCÁRIO
        SALDO ATUAL: R$ {saldo:.2f}
        NUMERO DE SAQUES: {numero_saques}
        MOVIMENTAÇÕES: {'Sem movimentações' if not extrato else extrato}
        """)

    elif opcao == 'q':
        print("Sair")
        break
    
    else:
        print("Operação inválida, por favor selecionar nuvamente a operação desejada !")