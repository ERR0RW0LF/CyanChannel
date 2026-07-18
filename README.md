# CyanChannel
Remote controll system writen in Rust using no AI. 

## Backend
One server to for handling connections.
Clients register with this server, most likely with a secure way to login.
Session tracking will be handled using redis.
Long term information like commands to run on next online or on schedule while be stored using a PostgreSQL db.
