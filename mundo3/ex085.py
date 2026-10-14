par = []
imp = []
num = []
for c in range(1, 8):  # Determinar números
    n = int(input(f'\033[0;34m{c}° número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
print('\033[1;33m-=' * 10)  # Mostrar resultado
num.append(par)
num.append(imp)
num[0].sort()
num[1].sort()
if num[0]:
    print(f'\033[1;32mOs valores pares digitados foram: {", ".join(str(v) for v in num[0])}')
else:
    print('\033[1;32mNão foram digitados valores pares.')
if num[1]:
    print(f'\033[1;32mOs valores ímpares digitados foram: {", ".join(str(v) for v in num[1])}')
else:
    print('\033[1;32mNão foram digitados valores ímpares.')
