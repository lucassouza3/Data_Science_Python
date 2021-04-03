import ipaddress #Possibilita cálculos com ip
ip = '192.168.0.0/24'
rede = ipaddress.ip_network(ip, strict=False)
print(rede)
for ip in rede:
    print(ip)