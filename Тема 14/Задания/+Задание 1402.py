# Решение
from itertools import product
for x, y in product("0123456", repeat=2):
    x1 = int(f"{y}{x}320", 7)
    x2 = int(f"1{x}3{y}3", 9)
    x3 = x1 + x2
    if x3 % 181 == 0:
        print(x3 // 181)





answer = 148

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1402, answer, '47d1e990583c9c67424d369f3414728e'))