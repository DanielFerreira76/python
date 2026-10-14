# Importações
from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

# Programa Principal
l = dado.leia('\033[0;34mDigite o preço: R$')
moeda.resumo(l, 50, 10)
