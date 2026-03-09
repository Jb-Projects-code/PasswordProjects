import getpass

FILE_NAME = "passwords.txt"

MASTER_PASSWORD = "password123"

attempt = getpass.getpass("Enter master password: ")
if attempt != MASTER_PASSWORD:
    print("Access denied!")
    exit()

def add_password(account, pwd):
    with open(FILE_NAME, "a") as f:
        f.write(f"{account}:{pwd}\n")
    print(f"Password for '{account}' saved!")

def get_password(account):
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                acc, pwd = line.strip().split(":", 1)
                if acc == account:
                    return pwd
        return "No password saved for this account"
    except FileNotFoundError:
        return "No passwords saved yet"

while True:
    print("\n--- PASSWORD MANAGER ---")
    print("1. Add password")
    print("2. Retrieve password")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        account = input("Enter account name: ")
        pwd = input("Enter password: ")
        add_password(account, pwd)

    elif choice == "2":
        account = input("Enter account name: ")
        print("Password:", get_password(account))

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")