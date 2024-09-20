menu = """
------------MENU------------
[D] Depositar
[S] Sacar
----------------------------
[E] Extrato     [X] Sair
----------------------------
=> """

saldo = 0
limite = 500
extrato = ""
menu_extrato = "EXTRATO"
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "X":
        break

    elif opcao == "D":
        valor = float(input("Valor do depósito: "))

        if valor <= 0:
            print("Valor invalido!")

        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    elif opcao == "S":
        valor = float(input("Valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = quantidade_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")

        elif excedeu_limite:
            print("Valor do saque acima limite!")

        elif excedeu_saques:
            print("Limite de saques diarios atingido!")

        elif valor <= 0:
            print("Valor invalido!")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            quantidade_saques += 1

    elif opcao == "E":
        print(menu_extrato.center(28, "-"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("----------------------------")
    else:
        print("Digito invalido! Tente novamente.")
