# Решение
from itertools import product

print("x y z w")
for x, y, z, w in product([0, 1], repeat=4):
    print(x, y, z, w, int((x == (not y)) <= (z <= (not w) and (w <= y))))


answer = "ywzx"

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 208, answer, '1f3ba34df7bed082a628be303ad291df'))