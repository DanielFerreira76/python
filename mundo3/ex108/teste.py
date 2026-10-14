# Código escrito por amor.
# Por ela. Pela nossa vida. Pelo futuro.

# Importações
import ex

# Programa Principal
while True:
    try:
        n = float(input('\033[0;34mDigite o preço: R$').replace(',', '.'))
        break
    except ValueError:
        print('\033[1;31mValor inválido. Tente novamente.')
print('~' * 30)
print(f'\033[1;32mA metade de {ex.moeda(n)} é {ex.moeda(ex.metade(n))}')
print(f'\033[1;32mO dobro de {ex.moeda(n)} é {ex.moeda(ex.dobro(n))}')
print(f'\033[1;32mAumentando 10%, temos {ex.moeda(ex.aumenta(n, 10))}')
