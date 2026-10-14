n = int(input('\033[0;34mDigite um número: '))
c = 1
ma = n
me = n
s = n
o = str(input('\033[0;34mQuer continuar? [S/N] ')).upper()[0]
while o == 'S':
    n = int(input('\033[0;34mDigite um número: '))
    s += n
    c += 1
    if n > ma:
        ma = n
    elif n < me:
        me = n
    o = str(input('\033[0;34mQuer continuar? [S/N] ')).upper()[0]
print('\033[1;32mVocê digitou {} números e a média entre eles é: {:.2f}'.format(c, s / c))
print('\033[1;32mO maior valor digitado foi {} e o menor foi {}'.format(ma, me))
