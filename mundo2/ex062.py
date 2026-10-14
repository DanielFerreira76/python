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
q = 10
while q > 0:
    q = int(input('\n\033[0;34mQuantos termos a mais quer mostrar? '))
    k = q
    while k > 0:
        c += 1
        n += r
        print('\033[1;32m -> {}'.format(n), end='')
        k -= 1
print('\033[1;35mProgressão finalizada com {} termos'.format(c))
