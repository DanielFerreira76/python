c = float(input('\033[0;34mQual o valor da casa? R$'))
s = float(input('\033[34mQual é o salário do comprador? R$'))
p = int(input('\033[34mEm quantos anos a compra será parcelada? '))
v = c / (p * 12)
print('\033[1;32mO valor das parcelas será de R${:.2f}'.format(v))
if v <= (s * 0.3):
    print('\033[1;32mEmpréstimo concedido!')
elif v > (s * 0.30):
    print('\033[1;31mEmpréstimo negado!')
