# Ports 

--- 

- A port is a logical communication endpoint used by applications and services to send and receive data.
- It has unique number assigned by IANA that identifies program or services 
- The number ranges from 0 to 65535 and has three categories
    - 0 to 1023      - Well known ports : used on server 
    - 1024 to  49151 - Registered ports : used on server
    - 49151 to 65535 - Dynamic/Private ports : used on client devices
- It is associated with IP address 
    - IP address identifies the device on network and port number determines the program or service on the server
- Ports are used together with transport layer protocols like TCP and UDP

## Netstat 
- It is a command to see the ip address and port number 
- netstat -n