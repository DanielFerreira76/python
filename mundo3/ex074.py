from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
ma = n[0]
me = n[0]
for c in n:
    if c > ma:
        ma = c
    if c < me:
        me = c
print(f'\033[1;32mOs números sorteados foram: {n}')
print(f'\033[1;34mO maior número é: {ma}')
print(f'\033[1;34mO menor número é: {me}')
