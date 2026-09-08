# Решение
from itertools import product

print("x y z w")
for x, y, z, w in product([0, 1], repeat=4):
    if not(((x <= y) or (z <= w)) and ((z == y) <= (w == x))):
        print(x, y, z, w)







answer = "yxwz"

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 204, answer, '1ed5bb3720986c091b8dc2704366e53d'))