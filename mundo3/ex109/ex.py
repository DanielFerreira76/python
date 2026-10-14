def metade(a, f=False):
    b = a / 2
    return b if not f else moeda(b)


def dobro(a, f=False):
    b = a * 2
    return b if not f else moeda(b)


def aumenta(a, b, f=False):
    c = a * (1 + (b / 100))
    return c if not f else moeda(c)


def moeda(a):
    b = f'R${a:.2f}'.replace('.', ',')
    return b


def diminui(a, b, f=False):
    c = a * (1 - (b / 100))
    return c if not f else moeda(c)