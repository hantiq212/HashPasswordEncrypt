import hashlib
import base64
import os

def short_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()[:16]

def encrypt(plaintext):
    if len(plaintext) > 50:
        raise ValueError("Plaintext terlalu panjang, maksimum 50 karakter")

    salt = base64.urlsafe_b64encode(os.urandom(4)).decode('utf-8').rstrip('=')
    data_encoded = base64.urlsafe_b64encode(plaintext.encode()).decode('utf-8').rstrip('=')
    integrity = short_hash(plaintext + salt)

    # Format compact: salt|data|hash
    result = f"{salt}|{data_encoded}|{integrity}"

    if len(result) > 100:
        raise ValueError(f"Hasil enkripsi melebihi 100 karakter! ({len(result)})")

    return result

if __name__ == "__main__":
    plaintext = input("Masukkan teks (maks 50 karakter): ").strip()
    encrypted = encrypt(plaintext)

    with open("encrypted.txt", "w") as f:
        f.write(encrypted)

    print(f"✅ Tersimpan di encrypted.txt ({len(encrypted)} karakter)")
