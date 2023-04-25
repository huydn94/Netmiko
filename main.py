from netmiko import ConnectHandler

#dictionary, object
Router = {
    "device_type": "cisco_ios",
    "ip": "10.18.8.157",
    "username": "vnpro",
    "password": "vnpro#123",
    "secret": "vnpro#321", #password enable
}
#user, privileges, config
connect=ConnectHandler(**Router) #unpack

#send command
print(connect.send_command("show ip interface brief"))
print("----------------------------")

connect.enable()
print(connect.send_command("show run"))

#send_config_set function
print(connect.send_config_set("hostname R1-Netmiko-Python"))

print(connect.send_config_set(["int e0/3", "no shut", "ip add 192.68.2.2 255.255.255.0"]))
connect.disconnect()

#use for loop
for i in range(1,4):
    print(connect.send_config_set(["int e0/"+ str(i), "no shut", "ip add 192.68."+str(i)+".2 255.255.255.0"]))


interface ={
    "e0/1": "192.168.12.1"
    "e0/2": "192.168.13.1"
    "e0/3": "192.168.15.1"
}
for i in interface:
    print(connect.send_config_set(["int "+i, "ip address "+interface[i]+" 255.255.255.0"]))
print(connect.send_command("show ip int bri"))