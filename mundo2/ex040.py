n1 = float(input('\033[0;34mPrimeira nota: '))
n2 = float(input('\033[0;34mSegunda nota: '))
m = (n1 + n2) / 2
print('\033[0;32mO aluno que tirou {} e {}, possui média {}'.format(n1, n2, m))
if m >= 7:
    print('\033[1;32mAluno aprovado')
elif 5 <= m < 7:
    print('\033[1;33mAluno de racuperação')
elif m < 5:
    print('\033[1;31mAluno reprovado')
