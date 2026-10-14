ma = 0
me = 0
for c in range(1, 6):
    p = float(input('\033[0;34mPeso da {}° pessoa: '.format(c)))
    if c == 1:
        ma = p
        me = p
    elif p > ma:
        ma = p
    elif p < me:
        me = p
print('\033[1;32mO maior valor digitado foi: {}'.format(ma))
print('\033[1;32mO menor valor digitado foi: {}'.format(me))
