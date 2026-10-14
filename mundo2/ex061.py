print('\033[1;33m=' * 25)
print('\033[1;35mGerador de PA')
print('\033[1;33m=' * 25)
n = int(input('\033[0;34mQual é o primeiro termo? '))
r = int(input('\033[0;34mQual é a razão da PA? '))
c = 1
print('\033[1;33m=' * 25)
print('\033[1;32m{}'.format(n), end='')
while c <= 9:
    c += 1
    n += r
    print(' -> {}'.format(n), end='')
