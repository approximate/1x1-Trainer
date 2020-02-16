from random import randint

while True:
    a = randint(1, 10)
    b = randint(1, 10)
    d = (a * b)
    print(a, 'x', b, '= ', end='')
    c = int(input(''))
    if c == d:
        print('Richtig!')
    else:
        print('Falsch\nGame Over')
        break
