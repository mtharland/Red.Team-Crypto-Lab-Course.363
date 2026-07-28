# Red.Team-Crypto-Lab-Course.363

It contains intentionally insecure services and matching attack scripts that show how weaknesses in cryptographic implementations lead directly to plaintext recovery, key extraction, or full system compromise.

The lab consists of five vulnerable services, five exploit scripts, and detailed writeups explaining each attack. Together, they form a cohesive red‑team learning environment suitable for Applied Cryptography coursework.

1. AES‑CBC Padding Oracle Attack

What was built
A vulnerable Flask service (padding_oracle_app) that decrypts AES‑CBC ciphertext and reveals whether the padding is valid. This is a classic cryptographic mistake: leaking padding validity allows attackers to recover plaintext one byte at a time.

What the attack does
The attack script (padding_oracle_attack.py) sends modified ciphertext blocks to the service and observes whether the padding is valid. Using this oracle, the attacker can:

- Recover plaintext without the key

- Exploit PKCS#7 padding rules

- Perform a full CBC padding oracle attack

This demonstrates how a single boolean leak (“valid padding: true/false”) becomes a full decryption vulnerability.

2. Timing Side‑Channel Password Attack

What was built
A Flask service (timing_attack_service) that compares a user‑supplied password to a secret password character by character, sleeping slightly for each correct character. This creates a measurable timing leak.

What the attack does
The attack script (timing_side_channel_attack.py) measures the response time for each password guess. Because the server sleeps longer when more characters are correct, the attacker can:

- Recover the password one character at a time

- Exploit microsecond‑level timing differences

- Demonstrate a real‑world side‑channel vulnerability

This shows how insecure string comparison functions can leak secrets even when the logic appears harmless.

3. Insecure PRNG (LCG) Attack

What was built
A Flask service (prng_service) that uses a predictable Linear Congruential Generator (LCG) to generate random numbers. LCGs are not cryptographically secure and can be broken with only a few outputs.

What the attack does
The attack script (prng_recovery_attack.py) collects several outputs from the PRNG and solves for the LCG parameters:

- Modulus m

- Multiplier a

- Increment c

Once these are known, the attacker can:

- Reconstruct the internal state

- Predict all future outputs

- Break any encryption relying on the PRNG

This demonstrates why cryptographically secure RNGs (CSPRNGs) are mandatory for secure systems.

4. One‑Time Pad (OTP) Key Reuse Attack

What was built
A Flask service (otp_reuse_service) that encrypts two different plaintext messages using the same XOR key. This violates the fundamental rule of one‑time pads: the key must only be used once.

What the attack does
The attack script (otp_xor_attack.py) XORs the two ciphertexts.

This gives a direct relationship between the plaintexts. Using crib‑dragging (guessing common English words), the attacker can:

- Recover portions of both plaintexts

- Expand guesses to reveal full messages

- Demonstrate how OTP reuse destroys perfect secrecy

This is a classic vulnerability seen in amateur crypto systems and CTF challenges.

5. RSA Low‑Exponent / No‑Padding Attack

What was built
A Flask service (rsa_vulnerable_service) that performs textbook RSA encryption with:

- No padding

- A small public exponent (e = 3)

- A small plaintext

This makes the ciphertext equal to m^3 mod n, which is vulnerable if m^3 < n.

What the attack does
The attack script (rsa_low_exponent_attack.py) computes the integer cube root of the ciphertext. If the plaintext is small enough, the cube root is the plaintext.

This demonstrates:

- Why RSA must use padding (OAEP)

- Why small exponents must be used carefully

- How textbook RSA is insecure

This is a real cryptographic vulnerability that has appeared in production systems.

This project demonstrates practical offensive cryptography skills through fully implemented attacks against intentionally vulnerable services. Each attack reinforces a core cryptographic concept and shows how implementation mistakes lead to real‑world exploitation.
