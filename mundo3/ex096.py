# Declarar funções
def area(a, b):
    t = a * b
    print(f'\033[1;32mA área total do terreno é de: {t:g}m².'.replace('.', ','))


# Ler dados
while True:
    try:
        l = float(input('\033[0;34mLargura(m): ').replace(',', '.'))
        break
    except ValueError:
        print('\033[1;32mValor inválido. Tente novamente.')
while True:
    try:
        c = float(input('\033[0;34mComprimento(m): ').replace(',', '.'))
        break
    except ValueError:
        print('\033[1;32mValor inválido. Tente novamente.')
area(l, c)
