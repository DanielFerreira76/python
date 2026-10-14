pessoas = []
maior = menor = 0
while True:
    nome = str(input('\033[0;34mNome: ')).strip().title()
    peso = float(input('\033[0;34mPeso: ').strip().replace(',', '.'))
    pessoas.append([nome, peso])
    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    op = str(input('\033[0;34mQuer continuar? [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        print('\033[1;31mResposta inválida. Tente novamente.')
        op = str(input('\033[0;34mQuer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('\033[1;33m-=' * 20)
if len(pessoas) == 1:
    print(f'\033[1;32mFoi cadastrada 1 pessoa')
else:
    print(f'\033[1;32mForam cadastradas {len(pessoas)} pessoas')
nomes_maior = [p[0] for p in pessoas if p[1] == maior]
print(f'\033[1;32mO maior peso foi de {maior:.2f} kg'.replace('.', ','), end='')
print(f'. Peso de {", ".join(nomes_maior)}')
nomes_menor = [p[0] for p in pessoas if p[1] == menor]
print(f'\033[1;32mO menor peso foi de {menor:.2f} kg'.replace('.', ','), end='')
print(f'. Peso de {", ".join(nomes_menor)}')
