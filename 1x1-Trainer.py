from random import randint

score = 0

while True:
    a = randint(1, 10)
    b = randint(1, 10)
    d = (a * b)
    print(a, 'x', b, '= ', end='')
    c = int(input(''))
    if c == d:
        print('Richtig!')
        score += 1
    else:
        print('Game Over')
        print("Deine Punkte =", score)
        break
