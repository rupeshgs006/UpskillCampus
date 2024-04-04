from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import os
import sqlite3

DATABASE_FILE = "passwords.db"

def generate_fernet_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Length of the derived key
        salt=salt,
        iterations=100000,  # Number of iterations (adjust as needed for security)
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

def create_password_database():
    conn = sqlite3.connect(DATABASE_FILE)
    conn.execute('''CREATE TABLE IF NOT EXISTS PASSWORD (
                        SITE VARCHAR(255) NOT NULL,
                        USER VARCHAR(255) NOT NULL,
                        ENCRYPTED_PASSWORD VARCHAR(255) NOT NULL,
                        FERNET_KEY VARCHAR(255) NOT NULL
                    );''')
    conn.commit()
    conn.close()

def retrieve_passwords():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT SITE, USER, ENCRYPTED_PASSWORD, FERNET_KEY FROM PASSWORD")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def insert_password(site, user, encrypted_password, fernet_key):
    conn = sqlite3.connect(DATABASE_FILE)
    conn.execute("INSERT INTO PASSWORD (SITE, USER, ENCRYPTED_PASSWORD, FERNET_KEY) VALUES (?, ?, ?, ?);",
                 (site, user, encrypted_password, fernet_key))
    conn.commit()
    conn.close()

def print_passwords(rows):
    print("SITE\t\tUSER\t\tPASSWORD")
    print("="*80)
    for row in rows:
        site, user, encrypted_password, fernet_key = row
        decrypted_password = decrypt_password(encrypted_password, fernet_key)
        print(f"{site}\t\t{user}\t\t{decrypted_password}")


def main():
    create_password_database()

    # Example usage
    site_name = input("Enter the site name: ")
    user_name = input("Enter the user name: ")
    password = input("Enter your password: ")

    salt = os.urandom(16)
    fernet_key = generate_fernet_key(password, salt)
    encrypted_password = encrypt_password(password, fernet_key)

    insert_password(site_name, user_name, encrypted_password, fernet_key)

    # Retrieve and print stored passwords
    stored_passwords = retrieve_passwords()
    print_passwords(stored_passwords)

if __name__ == "__main__":
    main()
