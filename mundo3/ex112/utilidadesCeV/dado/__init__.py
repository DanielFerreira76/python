def leia(a):
    while True:
        try:
            n = float(input(a).strip().replace(',', '.'))
            break
        except ValueError:
            print(f'\033[1;31mValor inválido. Tente novamente.')
    return n
