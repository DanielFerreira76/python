n = str(input('Digite o seu nome completo: '))
n.strip()
n1 = n.split()
print("""Seu primeiro nome é: {};
Seu ultimo nome é: {}.""".format(n1[0], n1[len(n1) - 1]))
