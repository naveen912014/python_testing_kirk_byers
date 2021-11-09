from netmiko import ConnectHandler
from getpass import getpass
import datetime

# Time for Execution:0:00:05 <- Without fast cli


device1 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
    "fast_cli": True,
}

net_connect = ConnectHandler(**device1)
start_time = datetime.datetime.now().replace(microsecond=0)
print(net_connect.find_prompt())

cfg = ["ip name-server 1.1.1.1","ip name-server 1.0.0.1","ip domain-lookup"]
output = net_connect.send_config_set(cfg)

print()
print("#" * 80)
print("CFG Change: ")
print(output)
print("#" * 80)
print()

ping_output= net_connect.send_command("ping google.com")

if '!!' in ping_output:
    print("Ping Successful:")
    print("\n\nPing Output: {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing Failed: {}\n\n".format(ping_output))

end_time = datetime.datetime.now().replace(microsecond=0)
net_connect.disconnect()

print(f'Time for Execution:{end_time-start_time}')