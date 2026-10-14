import ex

# Programa Principal
n = float(input('\033[0;34mDigite o preço: R$').replace(',', '.'))
print('~' * 30)
print(f'\033[1;32mA metade de R${n:.2f} é R${ex.metade(n):.2f}'.replace('.', ','))
print(f'\033[1;32mO dobro de R${n:.2f} é R${ex.dobro(n):.2f}'.replace('.', ','))
print(f'\033[1;32mAumentando 10%, temos R${ex.aumenta(n, 10):. 2f}'.replace('.', ','))
