p = float(input('\033[0;34mPeso: '))
a = float(input('\033[0;34mAltura: '))
imc = p / (a ** 2)
print('\033[0;32mIMC = {:.0f}'.format(imc))
if imc < 18.5:
    print('\033[1;33mA pessoa está abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('\033[1;32mA pessoa está no peso ideal')
elif 25 <= imc < 30:
    print('\033[1;33mA pessoa está em sobrepeso')
elif 30 <= imc < 40:
    print('\033[1;31mA pessoa está obesa')
elif imc >= 40:
    print('\033[1;31mA pessoa está em obesidade mórbida')
