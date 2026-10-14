# Código escrito por amor.
# Por ela. Pela nossa vida. Pelo futuro.

from datetime import datetime


# Coletar dados
pessoa = {'Nome': str(input('\033[0;34mNome: ').strip().title())}
while True:
    try:
        ano = int(input(f'\033[0;34mAno de Nascimento: '))
        break
    except ValueError:
        print('\033[1;31mValor inválido. Tente novamente.')
pessoa['Idade'] = datetime.now().year - ano
while True:
    try:
        pessoa['CTPS'] = int(input(f'\033[0;34mCarteira de Trabalho (0 se não tem): '))
        break
    except ValueError:
        print('\033[1;31mValor inválido. Tente novamente.')
if pessoa['CTPS'] > 0:
    while True:
        try:
            pessoa['Ano de Contratação'] = int(input(f'\033[0;34mAno de Contratação: '))
            break
        except ValueError:
            print('\033[1;31mValor inválido. Tente novamente.')
    while True:
        try:
            s = float(input(f'\033[0;34mSalário: \033[0;32mR$').replace(',', '.'))
            break
        except ValueError:
            print('\033[1;31mValor inválido. Tente novamente.')
    pessoa['Salário'] = f'R${s:.2f}'.replace('.', ',')
    pessoa['Idade de Aposentadoria'] = pessoa['Idade'] + ((pessoa['Ano de Contratação'] + 35) - datetime.now().year)

# Mostrar resultado
print('\033[1;33m-=' * 15)
for i, v in pessoa.items():
    print(f'\033[1;32m{i:<22} \033[1;35m-> \033[1;34m{v}')
