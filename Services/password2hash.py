import hashlib

def generate_hash():
    password = input("Enter the password you want to hash: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print(f"The hashed password is: {hashed_password}")

if __name__ == "__main__":
    generate_hash()
