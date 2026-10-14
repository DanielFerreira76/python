from time import sleep

nome = []
nota1 = []
nota2 = []
notas = [nota1, nota2]
media = []
aluno = [nome, notas, media]
o = 'S'
b = 0
while o == 'S':  # Cadastrar alunos
    nome.append(str(input('\033[0;34mNome: ').title().strip()))
    nota1.append(float(input('\033[0;34mNota 1: ').replace(',', '.')))
    nota2.append(float(input('\033[0;34mNota 2: ').replace(',', '.')))
    media.append((nota1[len(nome) - 1] + nota2[len(nome) - 1]) / 2)
    o = str(input('\033[0;34mQuer continuar? ').strip().upper()[0])
    while o not in 'SN':
        print('\033[1;31mValor inválido. Tente novamente.')
        o = str(input('\033[0;34mQuer continuar? ').strip().upper()[0])
print('\033[1;33m-=' * 20)  # Mostrar resultado
print(f"\033[1;35m{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print('\033[1;33m-' * 40)
for i in range(len(nome)):
    print(f'\033[1;32m{i:<4}{nome[i]:<10}{media[i]:>8.1f}'.replace('.', ','))
print('\033[1;33m-=' * 20)
while True:  # Mais opções
    b = int(input('\033[0;34mMostrar notas de qual aluno?(999 interrompe) '))
    if b == 999:
        break
    if b < 0 or b >= len(nome):
        print('\033[1;31mValor inválido. Tente novamente.')
    else:
        print(f'\033[1;32mAs notas do aluno {aluno[0][b]} são: {aluno[1][0][b]:.1f} e {aluno[1][1][b]:.1f}'.replace('.', ','))
        print('\033[1;33m-' * 40)
print('\033[0;32mFinalizando', end='')
sleep(0.75)
for c in range(0, 3):
    print('\033[0;32m.', end='')
    sleep(0.75)
print()
print('\033[1;35m<<< Volte Sempre! >>>')
