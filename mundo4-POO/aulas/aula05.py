class Pessoa:
    '''
Cria uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use:
variável = Pessoa(nome, idade)
    '''
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"

p1 = Pessoa("Daniel", 18)
p1.aniversario()
print(p1)

p2 = Pessoa("Mariana", 19)
print(p2)
print(p1.__getstate__())
print(Pessoa.__doc__)
