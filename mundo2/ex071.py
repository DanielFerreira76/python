saque = int(input('\033[0;34mDigite o valor que deseja sacar: R$'))
print('\033[1;33m=' * 25)
n50 = n20 = n10 = n01 = 0
while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        else:
            if saque >= 10:
                saque -= 10
                n10 += 1
            else:
                if saque >= 1:
                    saque -= 1
                    n01 += 1
    if saque == 0:
        break
print('\033[32mVocê leva:')
print(f'\033[32m{n50} notas de R$50.00\n{n20} notas de R$20.00\n{n10} notas de R$10.00\n{n01} notas de R$01.00')
