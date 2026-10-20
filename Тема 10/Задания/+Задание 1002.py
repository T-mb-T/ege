# Решение
from ipaddress import ip_network

count = 0
net = ip_network('122.159.136.144/29', False)
for ip in net:
    if f'{ip:b}'.count('1') % 4 != 0:
        count += 1
print(count)

answer = 5

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(10, 1002, answer, 'e4da3b7fbbce2345d7772b0674a318d5'))