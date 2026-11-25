class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos de idade"

p1 = Pessoa()
p1.nome = "Daniel"
p1.idade = 18
p1.aniversario()
print(p1.mensagem())

p2 = Pessoa()
p2.nome = "Mariana"
p2.idade = 19
print(p2.mensagem())
