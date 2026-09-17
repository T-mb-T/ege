# Решение
x = 0
for i in range(249999995, 894728062):
    N = bin(i)[2:]
    N = N + bin(i % 4)[2:]
    if int(N ,2) >= 1000000000 and int(N, 2) <= 1789456123:
        x += 1
print(x)



answer = 296046047

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 54, answer, '473b677ddfbedbb3d2e6d5e5980dc6e1'))