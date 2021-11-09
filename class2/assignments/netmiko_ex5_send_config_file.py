from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}

for device in (nxos1,nxos2):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_config_from_file(config_file="vlans.txt")
    print()
    print("#" * 80)
    print("CFG Change: ")
    print(output)
    print("#" * 80)
    print()
    save_out = net_connect.save_config()
    print()
    print("#" * 80)
    print("CFG Change: ")
    print(save_out)
    print("#" * 80)
    print()
    net_connect.disconnect()


