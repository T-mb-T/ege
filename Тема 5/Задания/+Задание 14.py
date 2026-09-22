n = []
for i in range(1, 150):
    r = bin(i)[2:]
    #11. 10. 1. 0
    r = r + bin(i % 4)[2:]
    print(int(r, 2), i)
    n.append(int(r, 2))
print(sorted(n))
print(len(n))
m = []
for i in range(148):
    m.append(sorted(n)[i + 1] - sorted(n)[i])
print(m)

answer = 19

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))