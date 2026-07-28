from flask import Flask, request, jsonify
import time

app = Flask(__name__)

SECRET_PASSWORD = "SuperSecret123!"

def insecure_compare(user_input: str, secret: str) -> bool:
    # Vulnerable: compares char-by-char and sleeps slightly
    for i in range(len(user_input)):
        if i >= len(secret) or user_input[i] != secret[i]:
            return False
        time.sleep(0.005)  # timing leak
    return len(user_input) == len(secret)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    pw = data.get("password", "")
    start = time.perf_counter()
    success = insecure_compare(pw, SECRET_PASSWORD)
    end = time.perf_counter()
    return jsonify({
        "success": success,
        "time": end - start
    })

if __name__ == "__main__":
    app.run(port=5002)
