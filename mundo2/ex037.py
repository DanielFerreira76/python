n = int(input('\033[0;34mDigite um número inteiro: '))
o = int(input('''\033[34mEscolha uma base para conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal
Sua opção: '''))
if o != 1 and o != 2 and o != 3:
    print('\033[31mOpção inválida, tente novamente')
else:
    print('\033[1;32mO número {} em'.format(n), end=' ')
    if o == 1:
        print('\033[32mbinário é {}'.format(bin(n)[2:]))
    elif o == 2:
        print('\033[32moctal é {}'.format(oct(n)[2:]))
    elif o == 3:
        print('\033[32mhexadecimal é {}'.format(hex(n)[2:]))
