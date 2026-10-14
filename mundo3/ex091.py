# Código escrito por amor.
# Por ela. Pela nossa vida. Pelo futuro.

from random import randint
from time import sleep
from operator import itemgetter

# Sortear os 4 dados
jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}
for k, v in jogadores.items():
    print(f'\033[1;35m{k} tirou {v} nos dados.')
    sleep(0.75)

# Classificações
print('\033[1;33m-=' * 15)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'\033[1;32m{i + 1}° Lugar: {v[0]} com {v[1]} pontos.')
