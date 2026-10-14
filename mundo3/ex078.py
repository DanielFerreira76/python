l = []
ma = me = 0
for c in range(0, 5):
    l.append(int(input(f'\033[0;34mDigite um número para a posição {c}: ')))
ma = l[0]
me = l[0]
for p in l:
    if p > ma:
        ma = p
    if p < me:
        me = p
print('\033[1;33m=' * 70)
print(f'\033[1;32mVocê digitou os valores:{l}')
print(f'\033[1;32mO maior valor digitado foi: {ma}, que está na posição:', end=' ')
for i, v in enumerate(l):
    if v == ma:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi: {me}, que está na posição:', end=' ')
for i, v in enumerate(l):
    if v == me:
        print(f'{i}...', end='')
