while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(10 * '====')
    if abs(n) != n:
        break
    for t in range(1, 10):
        r = n * t
        print(f'{t} x {n} = {r}')
    print(10 * '====')


