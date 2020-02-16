from random import randint

while True:
    a = randint(1, 10)
    b = randint(1, 10)
    d = (a * b)
    score = 0
    print(a, 'x', b, '= ', end='')
    c = int(input(''))
    if c == d:
        print('Richtig!')
        score + 1
    else:
        print('Falsch!\nGame Over')
        break
        print("Deine Punkte =", score)
