from random import randint
from time import sleep

jogos = []
num = []
print('\033[1;33m-=' * 20)
print('\033[1;35mJOGO DA MEGA SENA'.center(40))
print('\033[1;33m-=' * 20)
j = int(input('\033[0;34mQuantos jogos serão sorteados? '))  # Definir quantidade de jogos
print('\033[1;33m-=' * 20)  # Sortear os jogos
print(f'\033[1;35mSORTEANDO {j} JOGOS'.center(40))
for c in range(0, j):
    while len(num) < 6:
        n = randint(1, 60)
        if n not in num:
            num.append(n)
    jogos.append(num[:])
    num.clear()
    print(f'\033[1;32mJogo {c + 1}: {sorted(jogos[c])}')
    sleep(1)
