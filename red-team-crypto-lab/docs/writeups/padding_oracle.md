\# AES-CBC Padding Oracle Attack



\*\*Objective:\*\* Exploit a vulnerable AES-CBC decryption endpoint that leaks padding validity.



\*\*Background:\*\* AES-CBC with PKCS#7 padding can be attacked if a service reveals whether

padding is valid. This allows plaintext recovery one byte at a time.



\*\*Red Team Angle:\*\* Demonstrates how subtle crypto implementation details become

full plaintext disclosure in real systems.



