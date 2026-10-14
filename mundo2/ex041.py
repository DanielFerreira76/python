from datetime import date

a = date.today().year
p = int(input('\033[0;34mAno de nascimento: '))
i = a - p
print('\033[0;32mO atleta possui {} anos'.format(i))
if i <= 9:
    print('\033[1;32mA classificação dele é: mirim')
elif 9 < i <= 14:
    print('\033[1;32mA classificação dele é: infantil')
elif 14 < i <= 19:
    print('\033[1;32mA classificação dele é: junior')
elif 19 < i <= 25:
    print('\033[1;32mA classificação dele é: sênior')
elif i > 25:
    print('\033[1;32mA classificação dele é: master')
