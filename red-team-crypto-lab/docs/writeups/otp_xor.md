\# Many-Time Pad XOR Attack



\*\*Objective:\*\*  

Recover plaintexts when a one-time pad (OTP) key is reused across multiple messages.



\*\*Background:\*\*  

A one-time pad is only secure if the key is used once.  

If the same key encrypts multiple messages, the ciphertexts leak information:



`C1 XOR C2 = P1 XOR P2`



This gives attackers a direct relationship between plaintexts.



\*\*Attack Steps:\*\*  

1\. XOR two ciphertexts encrypted with the same OTP key.  

2\. The result is the XOR of the two plaintexts.  

3\. Use crib-dragging (guessing English words or known phrases) to align likely plaintext segments.  

4\. Recover portions of both plaintexts.  

5\. Expand guesses until full messages are revealed.



\*\*Impact:\*\*  

Plaintext recovery without knowing the key.  

Even partial guesses can unravel entire messages.



\*\*Red Team Angle:\*\*  

Many-time pad vulnerabilities appear in:  

\- Custom messaging apps  

\- Amateur crypto implementations  

\- CTF challenges  

\- Systems that misuse stream ciphers or reuse nonces  



This attack demonstrates how key reuse destroys the perfect secrecy of OTP.



