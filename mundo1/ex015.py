d = int(input('Quantos dias passou com o carro? '))
k = float(input('Quantos km foram rodados? '))
t = (d * 60) + (k * 0.15)
print('O valor a pagar é de: R${:.2f}'.format(t))
