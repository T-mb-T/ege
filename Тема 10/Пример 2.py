from ipaddress import ip_network
'''
net - Подсеть
'''

a = 0
for i in range(33):
    net = ip_network(f"169.25.132.59/{i}", False)
    if f"{net.network_address:b}".count("1") == 32 - i:
        for ip in net:
            if f"{ip:b}".count("1") == 11:
                a += 1
print(a)