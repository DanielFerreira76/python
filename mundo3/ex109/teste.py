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
print(f'\033[1;32mA metade de {ex.moeda(n)} é {ex.metade(n, f=True)}')
print(f'\033[1;32mO dobro de {ex.moeda(n)} é {ex.dobro(n, f=True)}')
print(f'\033[1;32mAumentando 10%, temos {ex.aumenta(n,10, f=True)}')
print(f'\033[1;32mReduzindo 13%, temos {ex.diminui(n,13, f=True)}')
