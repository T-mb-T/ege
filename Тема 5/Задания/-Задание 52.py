# Решение
for i in range(1, 100000):
    x = 0
    y = 0
    N = bin(i)[2:]
    for z in range(len(N)):
        if z % 2 == 0:
            if str(N)[z - 1] == "1":
                y += 1
        if z % 2 == 1:
            if str(N)[z - 1] == "0":
                x += 1
    if x - y == 5 or x - y == -5:
        print(x - y, i)
        break



answer = 511

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))