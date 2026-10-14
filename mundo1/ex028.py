from random import randint
from time import sleep

nc = randint(0, 5)
nj = int(input('Em qual número você acha que eu pensei? '))
print('PROCESSANDO...')
sleep(2)
print('-=' * 30)
if nj == nc:
    print('Você venceu! Eu realmente pensei no número {}.'.format(nc))
else:
    print('Perdeu! Eu pensei no número {} não no número {}.'.format(nc, nj))
