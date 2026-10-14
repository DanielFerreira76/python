s = 0
for c in range(1, 7):
    n = int(input('\033[0;34mDigite um número: '))
    if n % 2 == 0:
        s += n
print('\033[1;32mA soma dos números pares entre os números digitados é {}'.format(s))
