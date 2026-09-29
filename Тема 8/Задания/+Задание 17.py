# Решение
from itertools import product
even = '2468'
odd = '1357'
spisok = set()
count = 0
for p in product(odd, even, odd, even, odd, even, odd, even, odd, even, odd):
    p = ''.join(p)
    if all(p.count(x) < 5 for x in p):
        pass
for p in product(even, odd, even, odd, even, odd, even, odd, even, odd, even):
    p = ''.join(p)
    if all(p.count(x) < 5 for x in p):
        pass
print(count)
print(len(spisok))


answer = 8200800

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 17, answer, 'd67d496249f30f93dd6a7a6d84701d60'))