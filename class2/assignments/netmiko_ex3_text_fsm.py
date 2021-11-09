from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# lldpoutput
#[{'capabilities': 'B',
#  'local_interface': 'Gi0/0/0',
#  'neighbor': 'twb-sf-hpsw1',
#  'neighbor_interface': '17'}]

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

lldp_output = net_connect.send_command("show lldp neighbors", use_textfsm=True)
pprint(lldp_output)

for device in lldp_output:
    print(device['neighbor_interface'])
net_connect.disconnect()