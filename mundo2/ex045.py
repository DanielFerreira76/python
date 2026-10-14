from time import sleep
from random import randint

i = ('Pedra', 'Papel', 'Tesoura')
print('\033[1;35mPEDRA, PAPEL, TESOURA')
print('\033[1;33m=-=-=-=-=-=-=-=-=-=-=')
print('''\033[1;32m[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
print('\033[1;33m=-=-=-=-=-=-=-=-=-=-=')
j = int(input('\033[0;34mSua jogada: '))
c = randint(0, 2)
print('\033[1;33m=-=-=-=-=-=-=-=-=-=-=')
sleep(0.75)
print('\033[1;35mJO')
sleep(0.75)
print('\033[1;35mKEN')
sleep(0.75)
print('\033[1;35mPO!')
sleep(0.75)
print('\033[1;33m=-=-=-=-=-=-=-=-=-=-=')
print('\033[1;32mJogador jogou {}'.format(i[j]))
print('\033[1;32mComputador jogou {}'.format(i[c]))
print('\033[1;33m=-=-=-=-=-=-=-=-=-=-=')
if j == c:
    print('\033[1;33mEmpate')
elif j == 0 and c == 1 or j == 1 and c == 2 or j == 2 and c == 0:
    print('\033[1;31mComputador venceu')
elif c == 0 and j == 1 or c == 1 and j == 2 or c == 2 and j == 0:
    print('\033[1;32mJogador venceu')
