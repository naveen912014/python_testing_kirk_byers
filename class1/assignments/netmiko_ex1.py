from getpass import getpass
from netmiko import ConnectHandler
import datetime

current_date = str(datetime.datetime.now())

password = getpass()
net_connect = ConnectHandler(
    host="cisco3.lasthop.io",
    username="pyclass",
    password=password,
    device_type="cisco_ios",
    session_log=current_date+"_my_session.txt",
)

print(net_connect.find_prompt())
net_connect.disconnect()