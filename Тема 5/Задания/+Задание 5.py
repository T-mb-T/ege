# Решение
for i in range(1000, 2000):
    N = bin(i)[2:]
    N = N.replace('1','a')
    N = N.replace('0','b')
    N = N.replace('a','0')
    N = N.replace('b','1')
    N = int(N, 2)
    if i - N == 999:
        print(i)
        break





answer = 1011

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))