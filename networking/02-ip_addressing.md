# IP _Addressing

---
- An IP address (Internet Protocol address) is a unique number assigned to a device on a   network so it can be identified and communicate with other devices.
-  It has 4 sets of numbers(octets(ranges from 0 - 255)) and is seperated by 3 dots 
- IP addresses are usually assigned by a DHCP server, commonly running on the router.
- IP address has 2 parts Network id and Host id 

## Network ID
 - It identifies the network in which the device is connected.
 - It is same for all devices connected to same network 

## Host ID
- It identifies the device connected to the netwoek 
- It is different for all devices

---

## Types of IP address

### Public IP address
- It is the IP address that is assigned by ISP to the router 
- Public IP addresses are globally unique and routable on the internet 

### Private IP address
- It is the IP address that is assigned by router to the devices in a particular network 
- Private IP address can be same for devices in different network
- It cannot access internet by its own 

### Network Address Translation (NAT)
- It is a process used by a router to convert private IP addresses to a public IP address and vice versa.
- Since private IP addresses cannot be directly used on the internet, NAT allows devices in a private network to access the internet by translating their private IP to a public IP.
- When a response comes from the internet, NAT uses its translation table to convert the public IP back to the correct private IP.

### Working of NAT
- To identify which device initiated which connection, NAT uses a translation table, and in most cases it uses Port Address Translation (PAT).
- When a device ( 192.168.1.2) sends data to the internet, the router assigns a temporary port number to that connection.
- The router then replaces the private IP with its public IP (assigned by ISP) and maps it with that port number.
Example:
``` bash
192.168.1.2:4001 → 203.0.113.10:4001
```
- When the response comes back, it includes the same port number, and the router checks its translation table to forward it to the correct private device.
- Port numbers are dynamic and temporary, meaning they can change for each new connection.

---

## Default Gateway 
- A default gateway is a device (router) that forward the data from one network to another

## Subnet mask 
- It is a 32-bit number used alongside IP address to seperate network id and host id 
- It's structute is similar to IP address(eg: 255.255.255.0)
- In a common subnet mask like 255.255.255.0, the first three octets usually represent the network portion and the last octet represent host portion 
- For a computer to communicate with the another computer it checks if it is in same network or in different by checking the NID and uses switch if NID is same and uses router is NID is different

---

## Static and Dynamic IP address

### Static IP address
- It is the IP address that is assigned by the user manually and doesnt changes with time 
- Less common for normal user devices but important for servers and infrastructure 

### Dynamic IP address 
- It is the IP address that is assigned automatically from DHCP server and changes after some time 

#### DHCP (Dynamic Host Configuration Protocol)
- DHCP server assigns IP addresses to devices on a netwrok from its scope as a lease 
- Scope is a range of IP addresses that can be assigned by the DHCP 
- Lease is a amount of time an IP address is assigned to a computer. It is done so that when the devices leaves the network and its lease expires their ip address can be given to another devices so that the scope doesnt runout

##### Reserevation 
- It ensures that a specific device identified by thei MAC address always gets the same IP address 
- It is given to devices such as printer routers or servers 