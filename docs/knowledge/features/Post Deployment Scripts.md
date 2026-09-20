# Post Deployment Scripts

## Short Description

After deployment on a device the clients register with the server an gets the for it specific scripts.

The scripts depend on:

- OS
- Running Version
- Patches
- Software installed
- Current Privileges

-> First enum scripts to gather more info on the target.

-> Posable exploits get determent based on this data by the server.

These exploits should follow this structure when provided to the target

1. 