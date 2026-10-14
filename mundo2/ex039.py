from datetime import date

a = date.today().year
p = int(input('\033[0;34mQual o ano de nascimento? '))
i = a - p
print('\033[0;32mA pessoa nascida em {}, possui {} anos em {}'.format(p, i, a))
if i == 18:
    print('\033[1;32mDeve-se alistar imediatamente')
elif i < 18:
    print('\033[0;32mFaltam {} anos para alistar-se'.format(18 - i))
    print('\033[1;31mO alistamento deverá ser feito em {}'.format(p + 18))
elif i > 18:
    print('\033[0;32mJá deveria ter sido alistado há {} anos'.format(i - 18))
    print('\033[1;33mO alistamento deveria acontecer em {}'.format(p + 18))
