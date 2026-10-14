num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
for l in range(0, 3):  # Definir os valores
    for c in range(0, 3):
        num[l][c] = int(input(f'\033[0;34mDigite um valor para ({l}, {c}): '))
        if num[l][c] % 2 == 0:
            somapar += num[l][c]
print('\033[1;33m-=' * 20)  # Mostrar matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[0;35m[{num[l][c]:^5}]', end=' ')
    print()
maior = num[1][0]  # Mostrar mais informações
if num[1][1] > maior:
    maior = num[1][1]
if num[1][2] > maior:
    maior = num[1][2]
somater = num[0][2] + num[1][2] + num[2][2]
print('\033[1;33m-=' * 20)
print(f'\033[1;32mA soma dos valores pares é {somapar}.')
print(f'\033[1;32mA soma dos valores da terceira coluna é {somater}.')
print(f'\033[1;32mO maior valor da segunda linha é {maior}.')
