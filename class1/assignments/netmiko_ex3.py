from getpass import getpass
from netmiko import ConnectHandler



password = getpass()

device = {
    "host":"cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
 }

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
output=net_connect.send_command("show version")
print(output)

with open('outfile.txt', 'w') as file_obj_2:
    file_obj_2.write(output)
