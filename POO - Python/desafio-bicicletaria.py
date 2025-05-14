class Bicicletaria:
    
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self. valor = valor

    def buzinar(self):
        print ("Zoom !, Zoom !")

    def parar(self):
        print ("Parando !")

    def correr(self):
        print ("Correndo Zoooooooommmmm !")


    #def __str__(self):
        #return f"Bicicleta: Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}, Valor: R$ {self.valor}"
    
    def __str__(self): 
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicletaria("vermelha", "caloi", 2015, 700)
#b1.buzinar()
#b1.correr()
#b1.parar()
#print (b1.modelo,  b1.cor,  b1.ano, b1.valor)
print(b1)

