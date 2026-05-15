# TCP/IP Protocol

- A set of rules that governs how data is transferred over the internet 
- Data is not sent in one solid piece. Instead, it is broken down into small chunks called Data Packets 

---

# Packet Switching and  Circuit Switching

## Circuit Switching
- Sends data in a long, uninterrupted stream 
- This is inefficient because other computers must wait for the transmission to finish before they can use the same line 


## Packet Switching
- Packets travel independently across various devices and networks
- They don't have to follow a fixed path or arrive in a specific order 
- This makes the internet smoother and more efficient for billions of users 

---

# Structure of a Data Packet
- A typical packet consists of three main sections 
 
## Header 
- Contains source and destination IP addresses, port numbers, and sequence numbers 

## Payload
- The actual chunk of data being sent (e.g., a piece of a photo) \

## Trailer
- Informs the destination that the end of the packet has been reached and performs error checking 

--- 

# The Journey of Data

## Fragmentation
- An image or file is broken into hundreds or thousands of packets 

## Independent Routing
- Each packet finds the best route to the destination using its internal addressing 


## Reassembly
- The receiving device reads the sequence numbers to put the packets back in the correct order to reconstruct the original file 
