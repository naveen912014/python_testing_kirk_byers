from netmiko import ConnectHandler
from getpass import getpass
import datetime


#Time taken for Global Delay Factor for 2 is ( Time for Execution:0:00:01)
#Time taken for Global Delay Factor for 2 is (Time for Execution:0:00:07)

start_time = datetime.datetime.now().replace(microsecond=0)


device1 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
    #"global_delay_factor": 2,
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())


#output = net_connect.send_command("show lldp neighbors detail")
output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
print(output)
end_time = datetime.datetime.now().replace(microsecond=0)
net_connect.disconnect()
print(f'Time for Execution:{end_time-start_time}')