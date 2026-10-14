def metade(a):
    b = a / 2
    return b


def dobro(a):
    b = a * 2
    return b


def aumenta(a, b):
    c = a * (1 + (b / 100))
    return c


def moeda(a):
    b = f'R${a:.2f}'.replace('.', ',')
    return b
