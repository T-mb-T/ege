from numpy import  base_repr

for i in range(1, 100):
    N = str(base_repr(i, 3))
    if i % 3 == 0:
        N = "1" + N + '02'
    else:
        N = N + str(base_repr(i % 3 * 4))
    print(i, int(N, 3))
    if int(N, 3) < 250:
        print(i)




answer = 7

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 53, answer, '4e732ced3463d06de0ca9a15b6153677'))