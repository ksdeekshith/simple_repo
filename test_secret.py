import os

def main():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(f"Username: {username}")
    print(f"Password: {password}")

if __name__ == "__main__":
    main()

