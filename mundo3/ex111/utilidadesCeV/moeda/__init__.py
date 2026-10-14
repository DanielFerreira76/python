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


def resumo(a, b, c):
    print('\033[1;33m=' * 30)
    print('\033[1;35mRESUMO DO VALOR'.center(35))
    print('\033[1;33m=' * 30)
    print(f'\033[1;32mA metade de {moeda(a)} é {metade(a, f=True)}')
    print(f'\033[1;32mO dobro de {moeda(a)} é {dobro(a, f=True)}')
    print(f'\033[1;32mAumentando {b}%, temos {aumenta(a, b, f=True)}')
    print(f'\033[1;32mReduzindo {c}%, temos {diminui(a, c, f=True)}')
