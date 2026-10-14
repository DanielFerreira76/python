n = int(input('\033[0;34mDigite um número: '))
q = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;33m', end=' ')
        q += 1
    else:
        print('\033[1;31m', end=' ')
    print(c, end=' ')
print('\n\033[0;32mO número {} é divisível por {} números'.format(n, q))
if q <= 2:
    print('\033[1;32mO número {} é primo'.format(n))
else:
    print('\033[1;31mO número {} não é primo'.format(n))
