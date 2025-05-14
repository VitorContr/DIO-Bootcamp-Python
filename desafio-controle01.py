
# TODO: Itere sobre cada transação na lista:
    
# TODO: Adicione o valor da transação ao saldo   

# TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    

def calcular_saldo(transacoes):
    
    saldo = 0
    
    for i in transacoes:
      saldo += i

    return saldo


entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print("Saldo: R$ " + str(f'{float(resultado):.2f}').replace('.', ','))

