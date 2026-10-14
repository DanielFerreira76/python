# Ler dados do aluno
aluno = {'nome': str(input('\033[0;34mNome: ').strip().title())}
while True:
    try:
        aluno['nota'] = float(input(f'\033[0;34mNota de {aluno['nome']}: ').replace(',', '.'))
        break
    except ValueError:
        print('\033[1;31mValor inválido. Tente novamente.')

# Determinar situação
if aluno['nota'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['nota'] < 7:
    aluno['situação'] = 'Recuperação'
elif aluno['nota'] < 5:
    aluno['situação'] = 'Reprovado'

# Mostrar resultado
print('\033[1;33m-=' * 15)
print(f'\033[1;32mO nome é {aluno['nome']};')
print(f'\033[1;32mA nota é de {aluno['nota']:.2f};'.replace('.', ','))
if aluno['situação'] == 'Aprovado':
    print('\033[1;32m', end='')
elif aluno['situação'] == 'Recuperação':
    print('\033[1;33m', end='')
elif aluno['situação'] == 'Reprovado':
    print('\033[1;31m', end='')
print(f'A situação é {aluno['situação']}.')
