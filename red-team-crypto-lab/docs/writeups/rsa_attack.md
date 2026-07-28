\# RSA Low-Exponent / No-Padding Attack



\*\*Objective:\*\*  

Exploit RSA implementations that use small public exponents (e.g., e = 3) or omit padding, enabling direct mathematical recovery of plaintext.



\*\*Background:\*\*  

Textbook RSA is deterministic and vulnerable.  

If a message `m` is small enough that `m^e < n`, then:



`ciphertext = m^e mod n`  

and the attacker can compute the integer root of the ciphertext to recover `m`.



Without padding (like OAEP), RSA provides no semantic security.



\*\*Attack Steps:\*\*  

1\. Capture ciphertext from the vulnerable RSA endpoint.  

2\. Check if the public exponent is small (commonly e = 3).  

3\. Compute the integer cube root (or appropriate root) of the ciphertext.  

4\. If `m^e < n`, the cube root is the plaintext.  

5\. Validate the recovered message.



\*\*Impact:\*\*  

Instant plaintext recovery.  

No private key required.  

No brute force needed.



\*\*Red Team Angle:\*\*  

These vulnerabilities appear in:  

\- Legacy financial systems  

\- Student-built RSA implementations  

\- Custom cryptographic protocols  

\- Systems that misunderstand padding requirements  



This attack demonstrates why padding schemes like OAEP are mandatory and why small exponents must be used carefully.



