l = list()
i = list()
p = list()
while True:
    n = int(input('\033[0;34mDigite um número: '))
    o = str(input('\033[34mQuer continuar? '))[0].upper()
    l.append(n)
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
    if o == 'N':
        break
print('\033[1;33m-=' * 30)
print(f'\033[1;32mLista completa: {l}')
print(f'\033[1;32mNúmeros pares: {p}')
print(f'\033[1;32mNúmeros ímpares: {i}')
