while True:
    n = int(input('\033[0;34mDe qual número você quer ver a tabuada? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'\033[1;35m{n} \033[1;33m× \033[1;35m{c} \033[1;33m= \033[1;32m{n*c}')
print('\033[1;32mPrograma encerrado, volte sempre')
