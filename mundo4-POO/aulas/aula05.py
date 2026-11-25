class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos de idade"

p1 = Pessoa("Daniel", 18)
p1.aniversario()
print(p1.mensagem())

p2 = Pessoa("Mariana", 19)
print(p2.mensagem())
