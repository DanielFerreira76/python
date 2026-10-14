# Código escrito por amor.
# Por ela. Pela nossa vida. Pelo futuro.

# Importar funções
from time import sleep


# Definir funções
def contagem(a, b, c):
    print('\033[1;33m-=' * 20)
    print(f'\033[1;35mContagem de {a} até {b} de {c} em {c}.')
    sleep(2.5)
    if c < 0:
        c *= -1
    elif c == 0:
        c = 1
    if a < b:
        n = a
        while n <= b:
            print(f'\033[1;32m{n}', end=' ', flush=True)
            sleep(0.5)
            n += c
        print(f'\033[1;35mFIM!')
    else:
        n = a
        while n >= b:
            print(f'\033[1;32m{n}', end=' ', flush=True)
            sleep(0.5)
            n -= c
        print(f'\033[1;35mFIM!')


# Fazer as contagens
contagem(1, 10, 1)
contagem(10, 0, 2)
print('\033[1;33m-=' * 20)
print('\033[1;32mAgora é sua vez de personalizar a contagem!')
while True:
    try:
        a = int(input('\033[0;34mInício: '))
        break
    except ValueError:
        print('\033[1;32mValor inválido. Tente novamente.')
while True:
    try:
        b = int(input('\033[0;34mFim: '))
        break
    except ValueError:
        print('\033[1;32mValor inválido. Tente novamente.')
while True:
    try:
        c = int(input('\033[0;34mPasso: '))
        break
    except ValueError:
        print('\033[1;32mValor inválido. Tente novamente.')
contagem(a, b, c)
