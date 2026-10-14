# Código escrito por amor.
# Por ela. Pela nossa vida. Pelo futuro.

# Ler dados
gol = []
gols = 0
jogador = {'nome': str(input('\033[0;34mNome do jogador: ').strip().title())}
while True:
    try:
        g = int(input(f'\033[0;34mQuantas partidas {jogador["nome"]} jogou? '))
        break
    except ValueError:
        print('\033[1;31mValor inválido. Tente novamente.')
for a in range(0, g):
    while True:
        try:
            b = int(input(f'\033[0;34m     Quantos gols na {a + 1}° partida? '))
            break
        except ValueError:
            print('\033[1;31mValor inválido. Tente novamente.')
    gol.append(str(b))
    jogador['gols'] = gol
    gols += b

# Mostrar resultado 1
print('\033[1;33m-=\033[1;32m' * 20)
jogador['total'] = gols
print(jogador)

# Mostrar resultado 2
print('\033[1;33m-=' * 20)
print(f'\033[1;32mO nome do jogador é {jogador["nome"]}.')
print(f'\033[1;32mOs gols foram: {', '.join(gol)}.')
print(f'\033[1;32mO total do gols foi {gols}.')

# Mostrar resultado 3
print('\033[1;33m-=' * 20)
print(f'\033[1;32mO jogador {jogador['nome']} jogou {g} partidas.')
for c, d in enumerate(gol):
    print(f'\033[1;35m ->  \033[1;34mNa {c + 1}° partida, fez {d} gols.')
print(f'\033[1;32mFoi um total de {gols} gols.')
