# Решение
from itertools import permutations, product

sogl = list("".join(x) for x in permutations("РСМХ", 2))
glas = list("".join(x) for x in permutations("ООАА", 2))
spis = set()
for s in permutations("РОСОМАХА"):
    s = "".join(s)
    if all(x not in s for x in sogl) and all(y not in s for y in glas):
        spis.add(s)
print(len(spis))
#первый


sogl = "РСМХ"
glas = "ОА"
count = 0
spis = set()
for s in product(sogl, glas, sogl, glas, sogl, glas, sogl, glas):
    if s.count("А") == 2 and s.count("О") == 2 and s[0] != s[2] != s[4] != s[6] != s[2] and s[4] != s[0] != s[6]:
        s = "".join(s)
        spis.add(s)
for s in product(glas, sogl, glas, sogl, glas, sogl, glas, sogl):
    if s.count("А") == 2 and s.count("О") == 2 and s[1] != s[3] != s[5] != s[7] != s[3] and s[5] != s[1] != s[7]:
        s = "".join(s)
        spis.add(s)
print(len(spis))
#второй


count = 0
for p in product(glas, sogl, glas, sogl, glas, sogl, glas, sogl, glas):
    p = "".join(p)
    s = p[:8]
    s1 = p[1:]
    if p[1] != p[3] != p[5] != p[7] != p[3] and p[5] != p[1] != p[7]:
        if s.count("А") == 2 and s.count("О") == 2 and s1.count("А") == 2 and s1.count("О") == 2:
            count += 2
print(count)
#третий

answer = 288

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))