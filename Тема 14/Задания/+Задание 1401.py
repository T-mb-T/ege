# Решение
from itertools import product
for x, y in product("0123456789ABC", repeat=2):
    x1 = int(f"8{x}78{y}", 13)
    x2 = int(f"79{x}{y}7", 18)
    x3 = x1 + x2
    if x3 % 9 == 0:
        print(x3 // 9)





answer = 113024

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1401, answer, '436fc6a87245490c1c09148823eec9ff'))