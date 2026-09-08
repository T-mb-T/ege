# Решение
from itertools import product

print("x y z w f")
for x, y, z, w in product([0, 1], repeat=4):
    print(x, y, z, w, int((x == (y <= z)) and (y == (not(z <= w)))))






answer = "wzxy"

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 205, answer, 'c5e4e768af58cf865c4006af69319e62'))