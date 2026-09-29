# Решение
from itertools import product, permutations
#0123456789ABCDEF
count = 0
combine = list("".join(x) for x in product("DEF", repeat=2))
print(combine)
for p in product("0123456789ABCDEF", repeat=6):
    p = ''.join(p)
    if p[0] != "0":
        if p.count("5") > 0 and p.count("D") + p.count("E") + p.count("F") == 2 and any(x in p for x in combine):
            count += 1
print(count)





answer = 335241

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 84, answer, '85705f54f8b912d25a2eac2583e7093d'))