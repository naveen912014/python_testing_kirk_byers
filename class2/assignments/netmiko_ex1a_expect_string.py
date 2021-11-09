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
output = net_connect.send_command(
    command, expect_string=r"Protocol", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Target", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    ip_addr, expect_string=r"Repeat", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Datagram", strip_prompt=False, strip_command=False
)

output += net_connect.send_command(
    "\n", expect_string=r"Timeout", strip_prompt=False, strip_command=False
)

output += net_connect.send_command(
    "\n", expect_string=r"Extended", strip_prompt=False, strip_command=False
)

output += net_connect.send_command(
    "\n", expect_string=r"Sweep", strip_prompt=False, strip_command=False
)

output += net_connect.send_command(
    ip_addr, expect_string=r"#", strip_prompt=False, strip_command=False
)



print(output)
net_connect.disconnect()