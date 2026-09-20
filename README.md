# CyanChannel

Remote control system written in Rust using no AI.

## Backend


One server to for handling connections.
Clients register with this server, most likely with a secure way to login.
Session tracking will be handled using redis.
Long term information like commands to run on next online or on schedule while be stored using a PostgreSQL db.

## C2

The C2 hides behind a standart http website.

When the C2 is deployed in a network where ip addresses are randomized with no way to get a static ip the c2 will serve a second page under a specific location. This location changes based on for the server as well as the clients known patterns. The clients will first look for all ips hosting a webpage under a specified port, and after that will try to verify if a one is the c2.

## Clients

To avoid man in the middle attacks the client has something similar to a root certificate authority list build in. This list will be used to check if a server is the correct one. The use of a system with a root ca should allow for the use of multiple servers and that if one gets compromised the admin can just quickly spin up a new C2.

## MVP (minimum viable product)

Clients:
- Windows:
  - [ ] remote shells (reverse and bind)
  - [ ] command scheduling
  - [ ] persistence
  - [ ] Anti Virus detection and evasion
  - [ ] hidden and secure transport of encrypted data inside http requests (multiple layers of encryption)
  - [ ] finding C2 in a network with non static ips
- Linux:
  - [ ] remote shells (reverse and bind)
  - [ ] command scheduling
  - [ ] persistence
  - [ ] Anti Virus detection and evasion
  - [ ] hidden and secure transport of encrypted data inside http requests (multiple layers of encryption)
  - [ ] finding C2 in a network with non static ips
- Android:
  - [ ] remote shells (reverse)
  - [ ] command scheduling
  - [ ] persistence
  - [ ] hidden and secure transport of encrypted data inside http requests (multiple layers of encryption)
  - [ ] finding C2 in a network with non static ips
