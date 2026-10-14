# Importações
import ex

# Programa Principal
while True:
    try:
        n = float(input('\033[0;34mDigite o preço: R$').replace(',', '.'))
        break
    except ValueError:
        print('\033[1;31mValor inválido. Tente novamente.')
ex.resumo(n, 20, 15)
