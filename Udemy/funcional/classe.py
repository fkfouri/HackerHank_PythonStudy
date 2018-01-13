class Pessoa:

    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def obterNome(self):
        return self.nome

    def obterIdade(self):
        return self.idade

p1 = Pessoa('Fabio', 38)
p2 = Pessoa('Tiago', 35)
p3 = Pessoa('Cintia', 31)


pessoas = []
pessoas.append(p1)
pessoas.append(p2)
pessoas.append(p3)

for p in pessoas:
    print(p.obterNome()) 