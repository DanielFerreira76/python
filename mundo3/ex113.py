# Funções
def LeiaInt(a):
    while True:
        try:
            b = int(input(a))
            break
        except ValueError:
            print('\033[1;31mValor inválido. Tente novamente.')
    return b


def LeiaFloat(a):
    while True:
        try:
            b = float(input(a).replace(',', '.'))
            break
        except ValueError:
            print('\033[1;31mValor inválido. Tente novamente.')
    return b


# Programa Principal
n1 = LeiaInt('\033[0;34mDigite um número inteiro: ')
n2 = LeiaFloat('\033[0;34mDigite um número real: ')
print(f'\033[1;32mO valores digitados foram {n1} e {n2:g} respectivamente'.replace('.', ','))
