def menu():
    print('\033[1;33m-=' * 20)
    print('\033[1;35mMENU PRINCIPAL'.center(45))
    print('\033[1;33m-=' * 20)
    print('\033[1;32m1 - \033[1;34mVer pessoas cadastradas')
    print('\033[1;32m2 - \033[1;34mCadastrar nova pessoa')
    print('\033[1;32m3 - \033[1;34mSair do sistema')
    print('\033[1;33m-=' * 20)
    while True:
        try:
            a = int(input('\033[0;34mSua opção: '))
            while a > 3 or a < 1:
                print('\033[1;31mValor inválido, digite um número entre 1 e 3')
                a = int(input('\033[0;34mSua opção: '))
            break
        except ValueError:
            print('\033[1;31mValor inválido, digite um número inteiro válido')
    return a


def titulo(a):
    print('\033[1;33m-' * 40)
    print(f'\033[0;32mOpção {a}'.center(45))
    print('\033[1;33m-' * 40)

