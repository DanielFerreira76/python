o = 4
while o == 4:
    n1 = int(input('\033[0;34mDigite um número: '))
    n2 = int(input('\033[0;34mDigite outro número: '))
    o = 0
    while o < 4:
        print('\033[1;33m=' * 25)
        print('''\033[1;35mSelecione uma opção:
[ 1 ] soma
[ 2 ] multiplicação
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
        print('\033[1;33m=' * 25)
        o = int(input('\033[0;34mQual é a sua opção? '))
        print('\033[1;33m=' * 25)
        while o > 5:
            o = int(input('\033[1;31mOpção inválida! Tente novamente: '))
        if o == 1:
            print('\033[1;32mA soma entre {} e {} é de {}'.format(n1, n2, n1 + n2))
        elif o == 2:
            print('\033[1;32mA multiplicação entre {} e {} é de {}'.format(n1, n2, n1 * n2))
        elif o == 3:
            if n1 > n2:
                print('\033[1;32mO número {} é maior do que {}'.format(n1, n2))
            elif n1 < n2:
                print('\033[1;32mO número {} é maior do que {}'.format(n2, n1))
            elif n1 == n2:
                print('\033[1;32mOs números são iguais')
print('\033[1;32mPrograma Finalizado')
