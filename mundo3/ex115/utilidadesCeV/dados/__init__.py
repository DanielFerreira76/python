def LeiaInt(a):
    while True:
        try:
            b = int(input(a))
            break
        except ValueError:
            print('\033[1;31mValor inválido, digite um número inteiro')
    return b

