n = int(input('\033[0;34mDigite um número: [999 para parar] '))
s = n
c = 1
while n != 999:
    n = int(input('\033[0;34mDigite um número: [999 para parar] '))
    s += n
    c += 1
s -= 999
c -= 1
print('\033[1;32mA soma dos {} números digitados é {}'.format(c, s))
