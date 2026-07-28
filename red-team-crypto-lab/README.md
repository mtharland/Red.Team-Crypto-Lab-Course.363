\# Red Team Cryptography Attack Lab



A collection of offensive cryptographic attacks implemented against intentionally

vulnerable services. Built as a red-team focused project for Applied Cryptography 363.



\## Included Attacks



\- AES-CBC padding oracle attack

\- Timing side-channel password recovery

\- Insecure PRNG (LCG) keystream recovery

\- Many-time pad XOR attack

\- RSA low-exponent / no-padding attack



\## Structure



\- `vulnerable-services/` — intentionally insecure crypto services

\- `attacks/` — exploit scripts

\- `docs/` — diagrams and writeups

\- `tests/` — automated tests



\## Academic Context



Created for Applied Cryptography 363 to demonstrate practical exploitation of

cryptographic weaknesses from a red-team perspective.



\## Disclaimer



All vulnerabilities are intentionally created for educational and research purposes.

Do not use these techniques on systems you do not own or have explicit permission to test.



