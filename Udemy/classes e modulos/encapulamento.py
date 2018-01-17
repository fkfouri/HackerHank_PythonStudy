'''
Objetivo
    - Restringir/protege acessos a informacao
    - Variaveis e metodos tipo Private (basta colocar dois underscore na variavel na declaracao)
'''

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.__sobrenome = sobrenome

    def getNome(self):
        return self.nome

    def getSobrenome(self):
        return self.__sobrenome

p = Pessoa('Fabio','Kfouri')
print(p.nome) #acessa diretamente a variavel interna. nao esta protegida
print(p.getNome()) #acessa a funcao getNome

#print(p.sobrenome) #vai dar erro pois, a variavei esta protegida (private)
print(p.getSobrenome()) #somente a funcao getSobrenome eh capaz de externar a variavel privada