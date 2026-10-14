# Funções
def ficha(nome='<desconhecido>', gols=0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    else:
        nome = nome.strip().title()
    if not str(gols).isnumeric():
        gols = 0
    else:
        gols = int(gols)
    print(f'\033[1;32mO jogador {nome} fez {gols} gol(s).')

# Programa Principal
print('\033[1;33m-' * 20)
n = str(input('\033[0;34mQual o nome do jogador? '))
g = str(input('\033[0;34mQuantos gols? '))
ficha(n, g)
