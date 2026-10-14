t = 0
v = 0
g = 0
mi = 0
for c in range(1, 5):
    print('\033[1;33m=========')
    print('\033[1;35m{}° Pessoa'.format(c))
    print('\033[1;33m=========')
    n = str(input('\033[0;34mNome: '))
    i = int(input('\033[0;34mIdade: '))
    t += i
    if i > v:
        v = i
        nv = n
    s = str(input('\033[0;34mSexo[M/F] : ')).strip().upper()
    if s == 'F' and i < 20:
        mi += 1
print('\033[1;34mA média entre as idades é de {}'.format(t / 4))
print('\033[1;34mA pessoa mais velha tem {} anos e se chama {}'.format(v, nv))
if mi == 0:
    print('\033[1;31mNão existem mulheres menores de 20 anos')
else:
    if mi == 1:
        print('\033[1;32mExiste 1 mulher menor de 20 anos')
    else:
        print('\033[1;32mExistem {} mulheres menores de 20 anos'.format(mi))
