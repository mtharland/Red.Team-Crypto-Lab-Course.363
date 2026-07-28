\# Breaking an Insecure PRNG (LCG)



\*\*Objective:\*\*  

Recover the internal state and parameters of a Linear Congruential Generator (LCG) used for encryption, allowing full keystream reconstruction.



\*\*Background:\*\*  

An LCG follows the formula:  

`X(n+1) = (aX(n) + c) mod m`  

If an attacker observes several outputs, they can solve for `a`, `c`, and `m` using modular arithmetic.



Once the parameters are known, the entire keystream can be reproduced.



\*\*Attack Steps:\*\*  

1\. Capture multiple sequential outputs from the PRNG.  

2\. Use modular equations to solve for the multiplier `a`, increment `c`, and modulus `m`.  

3\. Reconstruct the PRNG’s internal state.  

4\. Generate the same keystream used by the encryption scheme.  

5\. Decrypt all messages encrypted with the PRNG.



\*\*Impact:\*\*  

Total compromise of encrypted communications.  

Any ciphertext produced by the PRNG becomes decryptable.



\*\*Red Team Angle:\*\*  

Weak PRNGs are common in:  

\- IoT devices  

\- Student-built crypto systems  

\- Lightweight embedded systems  

\- Amateur encryption libraries  



This attack highlights why cryptographically secure RNGs (CSPRNGs) are mandatory for any security-sensitive application.



