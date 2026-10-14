# Importações
from ex111.utilidadesCeV import moeda

# Programa Principal
while True:
    try:
        n = float(input('\033[0;34mDigite o preço: R$').replace(',', '.'))
        break
    except ValueError:
        print('\033[1;31mValor inválido. Tente novamente.')
moeda.resumo(n, 50, 10)
