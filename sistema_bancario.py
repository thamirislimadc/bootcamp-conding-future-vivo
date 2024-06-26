print("======================================")
print("BEM-VINDO AO BANCO TRID!")
print("======================================")

menu = """Selecione uma das seguintes opções:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()
    
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print("Depósito realizado com sucesso!\n")
        else:
            print("Operação inválida! Valor de depósito deve ser positivo.\n")
    
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor do saque: \n"))
            if valor > 0 and valor <= saldo and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!\n")
            elif valor > saldo:
                print("Saldo insuficiente!\n")
            elif valor > limite:
                print(f"Operação inválida! O valor máximo para saque é de R${limite:.2f}.\n")
            else:
                print("Operação inválida! Valor de saque deve ser positivo.\n")
        else:
            print("Limite de saques diários atingido!\n")
    
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("==============================\n")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.\n")

print("Obrigado por utilizar o Banco Trid!\n")
