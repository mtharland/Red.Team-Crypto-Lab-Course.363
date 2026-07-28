from flask import Flask, jsonify
import os

app = Flask(__name__)

KEY = os.urandom(64)  # reused key

def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

P1 = b"Attack at dawn with full force and no retreat."
P2 = b"Defend at dusk with minimal troops and caution."

C1 = xor_bytes(P1, KEY)
C2 = xor_bytes(P2, KEY)

@app.route("/messages", methods=["GET"])
def messages():
    return jsonify({
        "c1": C1.hex(),
        "c2": C2.hex()
    })

if __name__ == "__main__":
    app.run(port=5004)
