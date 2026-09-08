# Решение
from itertools import product

print('x y z w f1 f2')
for x, y, z, w in product([0, 1], repeat=4):
    print(x, y, z, w, int((x or not(y)) <= (w == z)), int((x or not(y)) == (w <= z)))




answer = "ywxz"

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 201, answer, '7379de4777f5748aa568b8d0bf8c3795'))