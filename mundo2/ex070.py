print('\033[1;33m=' * 11)
print('\033[1;35mLoja Zipele')
print('\033[1;33m=' * 11)
v = m = 0
pb = 999999999999999
while True:
    n = input('\033[0;34mNome do Produto: ')
    p = float(input('\033[0;34mPreço: R$'))
    if p < pb:
        nb = n
        pb = p
    v += p
    if p >= 1000:
        m += 1
    o = input('\033[0;34mQuer continuar?(S/N) ').upper()[0]
    if o == 'N':
        break
print('\033[1;33m=' * 25)
print(f'\033[1;32mO valor total da compra é de R${v:.2f}')
print(f'\033[1;32mTemos {m} produtos que custam mais de R$1000.00')
print(f'\033[1;32mO produto mais barato é {nb} que custa R${pb:.2f}')
