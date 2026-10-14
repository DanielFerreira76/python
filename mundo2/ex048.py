q = 0
n = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        q += 1
        n += c
print('\033[1;32mA soma dos {} valores solicitados é {}'.format(q, n))
