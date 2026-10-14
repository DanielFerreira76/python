n = str(input('Digite seu nome completo: '))
n0 = n.upper()
n1 = n.lower()
n2 = len(n) - n.count(' ')
n3 = n.split()[0]
n4 = len(n.split()[0])
print("""Seu nome em maiúsculas é: {};
Seu nome em minusculas é: {};
Seu nome tem {} caractéres;
Seu primeiro nome é {} e ele tem {} caractéres.""".format(n0, n1, n2, n3, n4))
