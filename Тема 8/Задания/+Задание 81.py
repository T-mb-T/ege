# Решение
from itertools import permutations, product
sogl = list("".join(x) for x in permutations("РСМХ", 2))
glas = list("".join(x) for x in permutations("ООАА", 2))
count = 0
spis = set()
for s in permutations("РОСОМАХА"):
    s = "".join(s)
    if all(x not in s for x in sogl) and all(y not in s for y in glas):
        count += 1
        spis.add(s)
print(len(spis))





answer = 288

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))