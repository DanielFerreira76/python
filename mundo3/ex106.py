# Funções
def pyhelp():
    while True:
        print('\033[1;33m~' * 15)
        print('\033[1;35mPyHelp'.center(15))
        print('\033[1;33m~' * 15)
        a = input('\033[0;34mFunção ou biblioteca: ').strip().lower()
        if a == 'fim':
            print('\033[1;33m~' * 15)
            print('\033[1;31mFIM'.center(15))
            print('\033[1;33m~' * 15)
            break
        else:
            print(f'\033[1;34m{help(a)}')

# Programa Principal
pyhelp()
