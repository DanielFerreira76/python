num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):  # Definir os valores
    for c in range(0, 3):
        num[l][c] = int(input(f'\033[0;34mDigite um valor para ({l}, {c}): '))
print('\033[1;33m-=' * 12)  # Mostrar matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[1;32m[{num[l][c]:^5}]', end=' ')
    print()
