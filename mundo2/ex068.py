from random import randint

print('\033[1;33m-=' * 10)
print('\033[1;35mJogo do Par ou Ímpar')
print('\033[1;33m-=' * 10)
while True:
    j = int(input('\033[0;34mJogue um valor: '))
    o = str(input('\033[0;34mPar ou Ímpar? ')).upper().split()[0]
    print('\033[1;33m-=' * 36)
    c = randint(0, 11)
    r = j + c
    print(f'\033[1;36mVocê jogou {j} e eu joguei {c}, resultando em {r},', end='')
    if o == 'P':
        if r % 2 == 0:
            print(f' que é par. \033[1;32mVocê venceu')
            print('\033[1;33m-=' * 36)
        else:
            print(f' que é ímpar. \033[1;31mVocê perdeu')
            print('\033[1;33m-=' * 36)
            break
    elif o == 'I':
        if r % 2 == 0:
            print(f' que é par. \033[1;31mVocê perdeu')
            print('\033[1;33m-=' * 36)
            break
        else:
            print(f' que é ímpar. \033[1;32mVocê venceu')
            print('\033[1;33m-=' * 36)
