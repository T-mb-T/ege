from ipaddress import ip_network
net = ip_network('68.203.243.87/27', False)
big = list(net.hosts())
print(big)
print(68 + 203 + 255 + 254)
