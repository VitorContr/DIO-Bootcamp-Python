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

def Depositar(valor):

    global saldo
    global extrato

    saldo += valor
    extrato += f"Depositar: R$ {valor:.2f}\n"
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")


def Sacar(valor): 

    global saldo
    global extrato
    global numero_saques
    
    if ( valor > saldo ): 
        print("Operação falhou! Você não tem saldo suficiente.")
    
    elif ( valor > limite ):
        print("Operação falhou! O valor do saque excede o limite.")
    
    elif ( numero_saques >= LIMITE_SAQUES ): 
        print("Operação falhou! Número máximo de saques excedido.")

    elif ( valor > 0 ):
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    else:
        print("Operação falhou! O valor informado é inválido.")

def Extrato():

    global saldo
    global extrato

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")



while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        Depositar(valor)
    
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))
        Sacar(valor)
            
    elif opcao == "e":
        Extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    

    


