from datetime import date

a = date.today().year
v = 0
n = 0
for c in range(1, 8):
    i = int(input('\033[0;34mDigite o ano de nascimento: '))
    if a - i >= 18:
        v += 1
    else:
        n += 1
print('\033[1;34mForam listados {} maiores de idade'.format(v))
print('\033[1;34mForam listados {} menores de idade'.format(n))
