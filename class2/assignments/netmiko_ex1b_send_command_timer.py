from netmiko import ConnectHandler
from getpass import getpass

#cisco4#ping
#Protocol [ip]:
#Target IP address: 8.8.8.8
#Repeat count [5]:
#Datagram size [100]:
#Timeout in seconds [2]:
#Extended commands [n]:
#Sweep range of sizes [n]:

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = "ping"
ip_addr = "8.8.8.8"
output = net_connect.send_command_timing(
    command, strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing(
    ip_addr,  strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing(
    "\n",  strip_prompt=False, strip_command=False
)

output += net_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False
)

output += net_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False
)

output += net_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False
)

output += net_connect.send_command_timing(
    ip_addr, strip_prompt=False, strip_command=False
)



print(output)
net_connect.disconnect()