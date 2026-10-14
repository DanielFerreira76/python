# Função
def maior(*n):
    print('\033[1;35mAnalisando os valores passados...')
    a = 0
    if len(n) > 0:
        for b in n:
            if b > a:
                a = b
            print(f'\033[1;34m{a}', end=' ', flush=True)
        print()
    if len(n) == 1:
        print('\033[1;32mFoi informado 1 valor.')
    elif len(n) == 0:
        print('\033[1;31mNenhum valor foi informado.')
    else:
        print(f'\033[1;32mForam informados {len(n)} valores.')
    print(f'\033[1;32mO maior valor informado foi {a}.')
    print('\033[1;33m-=' * 17)


# Programa
maior(1, 2, 3, 4, 5, 6)
maior()
maior(0, 456, 546456, 454545454)
maior(200)
