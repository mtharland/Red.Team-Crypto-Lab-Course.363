from flask import Flask, jsonify

app = Flask(__name__)

# Tiny demo RSA with e=3 and small message
n = 2351669  # demo modulus
e = 3
m = 1234     # small plaintext

c = pow(m, e, n)

@app.route("/encrypt", methods=["GET"])
def encrypt():
    return jsonify({
        "ciphertext": str(c),
        "e": str(e),
        "n": str(n)
    })

if __name__ == "__main__":
    app.run(port=5005)
