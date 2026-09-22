# Решение
from numpy import base_repr
x = []
for i in range(1, 111):
    N = base_repr(i, 3)
    if N[-1] == '0':
        N = N[-2]
    else:
        N = N + base_repr(int(N[-1]) * 5, 3)
    R = int(N, 3)
    x += [R]
    print(R, N, i)
print(sorted(x))





answer = 149

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 55, answer, '82aa4b0af34c2313a562076992e50aa3'))