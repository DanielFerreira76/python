n = list()
n.append(int(input('\033[0;34mDigite um número: ')))
print('\033[1;32mValor adicionado com sucesso!')
while True:
    o = input('\033[0;34mQuer continuar? ').upper()[0]
    if o == 'N':
        break
    a = int(input('\033[0;34mDigite um número: '))
    if a in n:
        print('\033[1;31mEsse valor já existe, não será adicionado')
    else:
        n.append(a)
        print('\033[1;32mValor adicionado com sucesso!')
n.sort()
print('\033[1;33m=' * 50)
print(f'\033[1;32mVocê digitou os valores: {n}')
