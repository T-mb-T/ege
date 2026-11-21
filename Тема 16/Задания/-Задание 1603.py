# Ре613шение
LIMIT = 100011
f = {0: 0}
for n in range(1, LIMIT):
    f[n] = f[n // 10] + n % 10
print("ЦИКЛ")
count = 0
for i in range(1, LIMIT - 1):
    if f[i] > f[i + 1]:
        count += 1
print(f)
print(count, 777181225 // 10)




answer = 77718122

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1603, answer, '383d228fc45e55c06236b5d6278e1765'))