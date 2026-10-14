# Importações
from utilidadesCeV import menu
from utilidadesCeV import opcoes
from utilidadesCeV import dados
from time import sleep

arq = 'pessoas.txt'

# Definir opção
while True:
    opc = menu.menu()
    menu.titulo(opc)
    sleep(1)
    if opc == 1:
        opcoes.mostrar()
    elif opc == 2:
        n = str(input('\033[0;34mNome: '))
        i = dados.LeiaInt('\033[0;34mIdade: ')
        opcoes.cadastrar(arq, n, i)
    elif opc == 3:
        print(f'\033[0;31m{'Saindo do sistema':>27}', end='')
        sleep(0.5)
        for c in range(0, 3):
            print('.', end='')
            sleep(0.5)
        print()
        print('\033[1;33m-=' * 20)
        break
