from random import randint

c = randint(0, 10)
k = 1
print('\033[1;35mSou seu computador...')
print('\033[1;35mPensei em um número de 0 a 10...')
print('\033[1;35mConsegue adivinhar em qual número eu pensei? ')
j = int(input('\033[0;34mEm qual número eu pensei? '))
while j != c:
    if j < c:
        print('\033[1;31mResposta errada, um pouco mais, tente novamente.')
    elif j > c:
        print('\033[1;31mResposta errada, um pouco menos, tente novamente.')
    j = int(input('\033[0;34mEm qual número eu pensei? '))
    k += 1
print('\033[1;32mParabéns! Eu pensei no número {}'.format(c))
if k != 1:
    print('\033[0;32mVocê conseguiu em {} tentativas'.format(k))
else:
    print('\033[0;32mVocê conseguiu em 1 tentativa')
