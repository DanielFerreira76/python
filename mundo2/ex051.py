print('\033[1;33m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\033[1;35m10 Primeiros termos de uma PA')
print('\033[1;33m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
p = int(input('\033[0;34mPrimeiro Termo: '))
r = int(input('\033[0;34mRazão: '))
d = p + (9 * r)
for c in range(0, 10):
    t = p + (c * r)
    if t == d:
        print('\033[1;32m{}'.format(t))
    else:
        print('\033[1;32m{}'.format(t), end='\033[1;36m -> ')
