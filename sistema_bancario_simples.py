menu = '''

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 0:
        print("===============Depositar===============")
        valor = float(input("Qual o valor a ser depositado? "))
        
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
        else:
            print("Operação falhou! O valor informador é inválido")

    elif opcao == 1:
        print("===============Sacar===============")
        valor = int(input("Infome o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')
        
        elif excedeu_saques:
            print('Operação falhou!. Numero máximo de saques excedido.')
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! O valor informado é inválido')

    elif opcao == 2:
        print('\n===============Extrato===============')
        print('Não foram realizados movimentações.' if not extrato else extrato)
        print(f'O seu saldo disponível é de R$ {saldo:.2f}')
        print('======================================')

    elif opcao == 3:
        print("Obrigado por utilizar os nossos serviços. Volte sempre!")
        break

    else:
        print("Opção inválida! Escolha apenas entre as opções disponíveis.")
