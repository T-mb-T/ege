# Решение
from itertools import permutations
from numpy import base_repr
'''
io = "0123456789ABCDE"
print(base_repr(855000000, 15))
x = set()
for p in permutations(io, 8):
    p = "".join(p)
    if int(p, 15) < 855000000 and p[0] != "0":
        x.add(p)
    if int(p, 15) >= 855000000:
        break
print(len(x))
'''


answer = 69189120

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 88, answer, '210095112b211a611c02a9a14cef2747'))