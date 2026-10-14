n = int(input('\033[0;34mDigite um número: '))
f = 1
print('\033[1;32mCalculando {}! = {}'.format(n, n), end=' ')
while n > 1:
    f *= n
    n -= 1
    print('×', end=' ')
    print('{}'.format(n), end=' ')
print('= {}'.format(f))
