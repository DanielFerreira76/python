cm = h = mm = 0
while True:
    print('\033[1;33m=' * 25)
    print('\033[1;35mCadastre uma pessoa')
    print('\033[1;33m=' * 25)
    i = int(input('\033[0;34mIdade: '))
    s = str(input('\033[0;34mSexo:(M/F) ')).upper()[0]
    print('\033[1;33m=' * 25)
    if i >= 18:
        cm += 1
    if s == 'M':
        h += 1
    if s == 'F' and i <= 20:
        mm += 1
    o = str(input('\033[0;34mQuer continuar?(S/N) ')).upper()[0]
    if o == 'N':
        print('\033[1;33m=' * 25)
        break
print(f'''\033[1;32mTemos {cm} pessoas com mais de 18 anos cadastradas
Temos {h} homens cadastrados
Temos {mm} mulheres com menos de 20 anos cadastradas''')
