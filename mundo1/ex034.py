s = float(input('Digite o valor do salário: R$'))
if s <= 1250:
    n = s * 1.15
    print('Com o aumento salarial de 15%, o salário de R${:.2f}, passa a ser de R${:.2f}.'.format(s, n))
else:
    n = s * 1.10
    print('Com o aumento salarial de 10%, o salário de R${:.2f}, passa a ser de R${:.2f}.'.format(s, n))
