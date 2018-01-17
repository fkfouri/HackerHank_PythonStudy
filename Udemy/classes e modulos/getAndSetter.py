'''
Objetivo
    - Restringir/protege acessos a informacao
    - Variaveis e metodos tipo Private (basta colocar dois underscore na variavel na declaracao)
'''

class Pessoa:
    def __init__(self):
        self.__nome = None

    @property #definicao do Get
    def nome(self):
        return self.__nome

    @nome.setter #definicao do Setter. Mesmo nome do GETTER
    def nome(self,nome):
        self.__nome = nome


p = Pessoa()
p.nome = 'Fabio'
print(p.nome) #acessa diretamente a propriedade

