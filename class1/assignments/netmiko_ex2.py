from getpass import getpass
from netmiko import ConnectHandler


hosts = ['nxos1.lasthop.io','nxos2.lasthop.io']

password = getpass()

for host in hosts:
    device = {
    "host": host,
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    }
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect()
