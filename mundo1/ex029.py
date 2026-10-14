v = int(input('Qual a velocidae do carro? '))
if v <= 80:
    print('Tudo certo! Tenha um bom dia.')
else:
    a = v - 80
    m = a * 77
    print('MULTADO! Você ultrapassou o limite de velocidade de 80km/h.')
    print('Sua multa vai custar R${},00.'.format(m))
    print('Dirija com segurança.')
