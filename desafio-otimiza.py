import datetime

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_usuarios = []
lista_contas = []

# --------------------------------------- USUARIO -------------------------------------------------------#

def adicionar_usuario():
  
    nome = input("Digite o nome do usuário: ")  # Recebe o nome do usuário
    
    cpf = input("Digite o CPF do usuário (apenas números): ")  # Recebe o CPF do usuário

    if not nome:
        print("O nome não pode estar vazio. Tente novamente.")
        return
    
    if any(usuario["cpf"] == cpf for usuario in lista_usuarios):  # Verifica duplicidade

        print("Este CPF já está cadastrado. Tente outro.")
        return

    # Adiciona o usuário à lista
    lista_usuarios.append( {"nome": nome, "cpf": cpf} )
    
    print(f"Usuário '{nome}' com CPF '{cpf}' adicionado com sucesso!")



def exibir_usuarios():
    if lista_usuarios:
        
        print("\nLista de usuários cadastrados:")
        
        for idx, usuario in enumerate(lista_usuarios, start=1):
            print(f"{idx}. {usuario}")
    
    else:
        print("\nA lista de usuários está vazia.")


# -------------------------------------------------------------------------------------------------------#

# --------------------------------------- CONTA ---------------------------------------------------------#

def adicionar_conta():
    
    numero_conta = len(lista_contas) + 1 
    agencia = "0001"

    for idx, usuario in enumerate(lista_usuarios, start=1):
        lista_contas.append( {"usuario": usuario, "agencia": agencia, "conta": numero_conta} )
        
    print(lista_contas)



# -------------------------------------------------------------------------------------------------------#

def Depositar(valor):

    global saldo
    global extrato

    saldo += valor
    extrato += f"Depositar: R$ {valor:.2f}\n"
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

# -------------------------------------------------------------------------------------------------------#

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

# -------------------------------------------------------------------------------------------------------#

def Extrato():

    global saldo
    global extrato

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")



# -------------------------------------------------------------------------------------------------------#
# --------------------------------------- MENU ---------------------------------------------------------#

menu = """

[1] Adicionar usuário

[2] Adicionar conta

[3] Exibir lista de usuários

[4] Depositar

[5] Sacar

[6] Extrato

[0] Sair

=> """


while True:

    opcao = input(menu)
    
    if opcao == "1":
        adicionar_usuario()
    
    elif opcao == "2":
        adicionar_conta()
    
    elif opcao == "3":
        exibir_usuarios()

    elif opcao == "4":
        valor = float(input("Informe o valor do depósito: "))
        Depositar(valor)
    
    elif opcao == "5":
        valor = float(input("Informe o valor do Saque: "))
        Sacar(valor)
    
    elif opcao == "6":
        Extrato()

    elif opcao == "0":
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")

# -------------------------------------------------------------------------------------------------------#