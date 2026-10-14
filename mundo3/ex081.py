n = list()
while True:
    n.append(int(input('\033[0;34mDigite um número: ')))
    o = str(input('\033[0;34mQuer continuar? '))[0].upper()
    if o == 'N':
        break
n.sort(reverse=True)
print('\033[1;33m-=' * 30)
print(f'\033[1;32mVocê digitou {len(n)} números')
print(f'\033[1;32mOs números digitados em ordem decrescente são: {n}')
if 5 in n:
    print('\033[1;32mVocê digitou o número 5')
else:
    print('\033[1;31mVocê não digitou o número 5')
