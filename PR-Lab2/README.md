## PR-Lab2

### Tasks
1. Implement a protocol atop UDP.
2. Make the connection secure, using a CA to get the public key of the receiver and encrypt data with it.

### Instructions Generate Private Key and Certificate Signing Request
```
$ openssl genrsa -des3 -passout pass:x -out server.pass.key 2048
...
$ openssl rsa -passin pass:x -in server.pass.key -out server.key
writing RSA key
$ rm server.pass.key
$ openssl req -new -key server.key -out server.csr
...
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:California
...
A challenge password []:
...
```