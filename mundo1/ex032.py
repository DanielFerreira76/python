from datetime import date

a = int(input('Digite um ano(Digite 0 se quer analisar o ano atual): '))
t = date.today().year
if a == 0:
    a = t
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print('O ano de {} é bissexto.'.format(a))
    else:
        print('O ano de {} não é bissexto.'.format(a))
else:
    if a < t:
        if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            print('O ano de {} foi bissexto.'.format(a))
        else:
            print('O ano de {} não foi bissexto.'.format(a))
    else:
        if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            print('O ano de {} será bissexto.'.format(a))
        else:
            print('O ano de {} não será bissexto.'.format(a))
