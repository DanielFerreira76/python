tupla = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
         'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
         'São Paulo', 'Atletico-PR', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-=' * 5, 'Placar Geral', '=-' * 5)
for c in range(0, len(tupla)):
    print(f'Time: {tupla[c]}, Posição: {c + 1}º.')
print('\n')
print('-=' * 5, '5 Primeiros Colocados', '=-' * 5)
for k in range(0, 5):
    print(f'Time: {tupla[k]}, Posição: {k + 1}º')
print('\n')
print('-=' * 5, '5 Últimos Colocados', '=-' * 5)
for i in reversed(range(20)):
    print(f'Time: {tupla[i]}, Posição: {abs(i + 1)}º')
for i in range(20)[14:20]:
    print(f'Time: {tupla[i]}, Posição: {abs(i + 1)}º')
print('\n')
print('-=' * 5, 'Lista em Ordem Alfabética', '=-' * 5)
ordem = sorted(tupla)
for g in ordem:
    print(g)
print('\n')
descobrir = ordem.index('Chapecoense')
print('-=' * 5, 'Posição do Chapecoense', '=-' * 5)
print(f'Posição do Chapecoense: {descobrir + 1}º Lugar.')
print('\n')
