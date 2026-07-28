import requests

def test_oracle_endpoint():
    url = "http://localhost:5001/decrypt"
    sample = {
        "ciphertext": ("00" * 16),
        "iv": ("00" * 16)
    }
    r = requests.post(url, json=sample)
    assert "valid" in r.json()

if __name__ == "__main__":
    test_oracle_endpoint()
    print("Padding oracle endpoint test passed.")
