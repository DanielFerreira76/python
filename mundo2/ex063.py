print('\033[1;33m=' * 25)
print('\033[1;35mSequência de Fibonacci')
print('\033[1;33m=' * 25)
q = int(input('\033[0;34mQuantos termos quer mostrar? '))
if q == 1:
    print('\033[1;32m0')
else:
    q -= 2
    t1 = 0
    t2 = 1
    print('\033[1;32m{} -> {}'.format(t1, t2), end=' ')
    while q > 0:
        t3 = t1 + t2
        print('-> {}'.format(t3), end=' ')
        t1 = t2
        t2 = t3
        q -= 1
print('\n\033[1;36mFim')
