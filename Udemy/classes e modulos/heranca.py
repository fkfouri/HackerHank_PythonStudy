#Super Classe que sera herdada
class Transport:
    def __init__(self, nome, peso, preco):
        self.nome = nome
        self.peso = peso
        self.preco = preco

    def getNome(self):
        return self.nome

    def getPeso(self):
        return self.peso

    def getPreco(self):
        return self.preco


#nome da classe herdando a super classe Transporte
class Carro(Transport):
    def __init__(self, nome, peso, preco, preco_seguro):
        #chamada da super classe
        Transport.__init__(self, nome,peso,preco) 
        self.preco_seguro = preco_seguro

    def getPrecoSeguro(self):
        return self.preco_seguro




t = Transport("Fusca",500, 4000.00)
print(t.getNome(), t.getPeso())

u = Carro("Passat",800,5550.0,800)
print(u.getNome(), u.getPreco(), u.getPrecoSeguro() )