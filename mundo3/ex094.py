# Ler dados
c = l = 0
pessoas = []
mulheres = []
pessoas_acima = []
acima = {}
pessoa = {}

while True:
    pessoa['nome'] = str(input('\033[0;34mNome: ').strip().title())
    s = str(input('\033[0;34mSexo (M/F): ').strip().upper()[0])
    while s not in 'MF':
        print('\033[1;31mValor inválido. Tente novamente.')
        s = str(input('\033[0;34mSexo (M/F): ').strip().upper()[0])
    pessoa['sexo'] = s
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    while True:
        try:
            i = int(input(f'\033[0;34mIdade: '))
            break
        except ValueError:
            print('\033[1;31mValor inválido. Tente novamente.')
    pessoa['idade'] = i
    l += i
    pessoas.append(pessoa.copy())
    c += 1
    o = str(input('\033[0;34mQuer continuar (S/N)? ').strip().upper()[0])
    while o not in 'SN':
        print('\033[1;31mValor inválido. Tente novamente.')
        o = str(input('\033[0;34mQuer continuar (S/N)? ').strip().upper()[0])
    if o == 'N':
        break

# Realizar calculos
m = float(l / len(pessoas))
for a in pessoas:
    if a['idade'] >= m:
        acima['nome'] = a['nome']
        acima['sexo'] = a['sexo']
        acima['idade'] = a['idade']
        pessoas_acima.append(acima.copy())

# Mostrar resultados
print('\033[1;33m-=' * 20)
if c == 1:
    print(f'\033[1;32mA) Ao todo temos 1 pessoa cadastrada.')
else:
    print(f'\033[1;32mA) Ao todo temos {c} pessoas cadastradas.')
print(f'\033[1;32mB) A média de idade é de {m:.0f} anos.')
if len(mulheres) >= 1:
    print(f'\033[1;32mC) As mulheres cadastradas foram: {", ".join(mulheres)}.')
else:
    print(f'\033[1;32mC) Nenhuma mulher foi cadastrada.')
print('\033[1;32mD) Lista de pessoas que tem idade acima da média: ')
for i in pessoas_acima:
    print(f'\033[1;34m  nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}')
