n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
     'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'quatorze', 'quinze',
     'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
o = int(input('\033[0;34mDigite um número entre 0 e 20: '))
while o > 20:
    o = int(input('\033[1;31mResposta inválida!\033[0;34m Digite um número entre 0 e 20: '))
print(f'\033[1;32mVocê digitou o número {n[o]}')
