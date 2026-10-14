km = float(input('Qual é a distância da viagem? '))
if km >= 200:
    p = km * 0.45
else:
    p = km * 0.5
print('A sua passagem custará R${:.2f}.'.format(p))
