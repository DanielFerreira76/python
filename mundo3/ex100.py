# Importações
from random import randint


# Funções
def sorteia(a):
    for b in range(0, 5):
        a.append(randint(1, 10))
    print(f'\033[1;32mSorteando 5 valores: \033[1;35m', end='')
    print(f'{a}'.replace('[', '').replace(']', ''))
    print('\033[1;32m')


def somapar(a):
    b = 0
    for c in a:
        if c % 2 == 0:
            b += c
    print(f'\033[1;32mSomando os valores pares de ', end='')
    print(f'{a}, temos {b}.'.replace('[', '').replace(']', ''))
    print(f'\033[1;32m')


# Programa
n = []
sorteia(n)
somapar(n)
