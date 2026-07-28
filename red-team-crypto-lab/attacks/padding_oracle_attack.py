import requests

URL = "http://localhost:5001/decrypt"

def oracle(ciphertext: bytes, iv: bytes) -> bool:
    r = requests.post(URL, json={
        "ciphertext": ciphertext.hex(),
        "iv": iv.hex()
    })
    return r.json()["valid"]

def demo():
    # This is a placeholder demo showing how you'd call the oracle.
    # In a full implementation, you'd modify ciphertext bytes to recover plaintext.
    import os
    ct = os.urandom(16)
    iv = os.urandom(16)
    is_valid = oracle(ct, iv)
    print(f"Oracle response (valid padding?): {is_valid}")

if __name__ == "__main__":
    demo()
