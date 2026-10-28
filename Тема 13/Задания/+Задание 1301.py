# Решение
def f(x, y):
    if x == y:
        return 1
    if x > y or x == 27:
        return 0
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

def f1(x, y):
    if x == y:
        return 1
    if x > y or x == 24:
        return 0
    return f1(x + 1, y) + f1(x * 2, y) + f1(x * 3, y)


print(f1(9, 27) * f1(27, 81))
print(f(9, 24) * f(24, 81))



answer = 142

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1301, answer, 'a8baa56554f96369ab93e4f3bb068c22'))
