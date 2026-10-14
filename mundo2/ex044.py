v = float(input('\033[0;34mValor da compra: R$'))
print('''\033[0;32mSelecione qual será o meio de pagamento:
[ 1 ] À vista
[ 2 ] À vista no cartão
[ 3 ] Em 2x no cartão
[ 4 ] Em 3x ou mais no cartão''')
o = int(input('\033[0;34mSua opção: '))
if o == 1:
    d = v * 0.90
    print('\033[1;32mSua compra de R${:.2f}, custará no final R${:.2f}'.format(v, d))
elif o == 2:
    d = v * 0.95
    print('\033[1;32mSua compra de R${:.2f}, custará no final R${:.2f}'.format(v, d))
elif o == 3:
    print('\033[1;32mAs parcelas serão 2 de R${:.2f}'.format(v / 2))
    print('\033[1;32mNo final sua compra custará R${:.2f}'.format(v))
elif o == 4:
    p = int(input('\033[0;34mEm quantas parcelas? '))
    d = v * 1.2
    print('\033[1;32mAs parcelas serão {} de R${:.2f}'.format(p, d / p))
    print('\033[1;32mSua compra de R${:.2f}, custará no final R${:.2f}'.format(v, d))
else:
    print('\033[1;31mValor inválido, tente novamente')
