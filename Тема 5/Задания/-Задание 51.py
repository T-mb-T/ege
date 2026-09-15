# Решение
#i = 427
#N = bin(i)[2:-5]
#print(N)
#print(int(N, 2))
#for i in range(1111111110, 1444444416):
print(bin(1111111110))
print(bin(1444444416))
print(int(str(10000100011101000110101110), 2))
print(int(str(10101100001100001111001000), 2))
x = int(str(10101100001100001111001000), 2) - int(str(10000100011101000110101110), 2)
print(x)
answer = 10416667

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 51, answer, '389499b02f30212486e408cd73a5bc50'))