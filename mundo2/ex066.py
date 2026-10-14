s = c = 0
while True:
    n = int(input('\033[0;34mDigite um número:(999 para parar) '))
    c += 1
    s += n
    if n == 999:
        s -= 999
        c -= 1
        break
print(f'\033[1;32mForam digitados {c} números e a soma deles é igual a {s}')
