from flask import Flask, request, jsonify
from Crypto.Cipher import AES
import os

app = Flask(__name__)

KEY = os.urandom(16)

def pkcs7_unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    if pad_len == 0 or pad_len > 16:
        raise ValueError("Bad padding")
    if data[-pad_len:] != bytes([pad_len]) * pad_len:
        raise ValueError("Bad padding")
    return data[:-pad_len]

def decrypt_cbc(ciphertext: bytes, iv: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return pkcs7_unpad(plaintext)

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    ct = bytes.fromhex(data["ciphertext"])
    iv = bytes.fromhex(data["iv"])
    try:
        decrypt_cbc(ct, iv)
        return jsonify({"valid": True})
    except Exception:
        return jsonify({"valid": False})

if __name__ == "__main__":
    app.run(port=5001)
