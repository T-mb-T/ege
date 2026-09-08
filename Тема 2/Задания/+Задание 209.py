# Решение
from itertools import product

print("x y z w")
for x, y, z, w in product([0,1], repeat=4):
    if (w == (not (z == y))) and (z == (y <= x)):
        print(x, y, z, w)




answer = "wxzy"

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 209, answer, 'd68899696c79e465e2a3547b4dc50435'))