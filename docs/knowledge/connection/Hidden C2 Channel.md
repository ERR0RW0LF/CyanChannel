# Hidden C2 Channels

## Port Knocking and Single Packet Authorization (SPA)

Implant monitors all the network traffic passively using raw sockets without binding to a specific port.

How it works: The controller sends a specific sequence of closed-port connection attempts (Port Knocking) or a single, cryptographically signed packet (SPA) to the host.

The Trigger: The implant detects this precise sequence or payload, verifies it, and then initiates an outbound connection or opens a temporary listening port to receive commands.

## 


## Comparison

| Feature | Port Knocking | Single Packet Authorization | type3 |
| :------ | ----- | ----- | ----- |
|         |       |       |       |