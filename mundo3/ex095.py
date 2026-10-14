# Ler dados
t = []
while True:
    gols = 0
    gol = []
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
        gols += b
        gol.append(str(b))
    jogador['gols'] = gol[:]
    jogador['total'] = gols
    t.append(jogador.copy())

    while True:
        o = str(input('\033[1;32mQuer continuar (S/N)? ').strip().upper()[0])
        if o in 'SN':
            break
        else:
            print('\033[1;31mValor inválido. Tente novamente.')
    if o == 'N':
        break

# Mostrar resultado
print('\033[1;33m-=' * 17, '-')
print(f'\033[1;32m{"cod":<3} {"nome":<14} {"gols":<10} {"total":<5}')
print('\033[1;33m-' * 35)
for i, a in enumerate(t):
    print(f'\033[1;34m{i + 1:>3} {a["nome"]:<14} {", ".join(a["gols"]):<10} {a["total"]:<5}')
print('\033[1;33m-' * 35)

# Mostrar mais dados
while True:
    while True:
        try:
            n = int(input('\033[0;34mMostrar dados de qual jogador(999 para parar)? '))
            break
        except ValueError:
            print('\033[1;31mValor inválido. Tente novamente.')

    if n == 999:
        break
    if n < 1 or n > len(t):
        print('\033[1;31mValor inválido. Tente novamente.')
    else:
        print('\033[1;33m-' * 35)
        print(f'\033[1;35mLevantamento do jogador {t[n - 1]["nome"]}')
        print(f'\033[1;32mO jogador {t[n - 1]["nome"]} jogou {len(t[n - 1]["gols"])} partidas.')
        for c, d in enumerate(t[n - 1]["gols"]):
            print(f'\033[1;35m ->  \033[1;34mNa {c + 1}° partida, fez {d} gols.')
        print(f'\033[1;32mFoi um total de {t[n - 1]["total"]} gols.')
        print('\033[1;33m-' * 35)
print('\033[1;33m-' * 35)
print('\033[1;32mEncerrando...')
