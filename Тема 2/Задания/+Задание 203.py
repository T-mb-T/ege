# Решение
from itertools import product

print("x y z w u")
for x, y, z, w, u in product([0, 1], repeat=5):
    if (((x <= y) and (z == (not w))) <= (u == (x or z))) == 0:
        print(x, y, z, w, u)






answer = "wzyxu"

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 203, answer, 'b83215ff76ddd410e32571919b78d0eb'))