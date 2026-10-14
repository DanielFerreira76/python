from time import sleep

for c in range(10, -1, -1):
    sleep(1)
    print('\033[0;32m{}'.format(c))
print('\033[1;32mAcabou')
