c9 = 0
n1 = int(input('\033[0;34mDigite um número: '))
n2 = int(input('\033[0;34mDigite um número: '))
n3 = int(input('\033[0;34mDigite um número: '))
n4 = int(input('\033[0;34mDigite um número: '))
if n1 == 9:
    c9 += 1
if n2 == 9:
    c9 += 1
if n3 == 9:
    c9 += 1
if n4 == 9:
    c9 += 1
n = (n1, n2, n3, n4)
print(f'\033[1;32mOs números digitados foram: {n}')
if c9 == 0:
    print('\033[1;31mNão foram digitados nenhum número 9')
else:
    print(f'\033[1;32mO número 9 foi digitado {c9} vezes')
if 3 in n:
    print(f'\033[1;32mO número 3 foi digitado na posição {n.index(3) + 1}')
else:
    print('\033[1;31mO número 3 não foi digitado')
print('\033[1;32mOs números pares digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(f'{c}', end=' ')
