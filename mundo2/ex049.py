n = int(input('\033[0;34mDigite um número para ver sua tabuada: '))
print('\033[1;33m-=' * 20)
for c in range(1, 11):
    print('\033[1;32m{} X {} = {}'.format(n, c, n * c))
print('\033[1;33m-=' * 20)
