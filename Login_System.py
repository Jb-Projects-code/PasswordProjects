username = "admin"
password = "secure123"

attempts = 3

while attempts > 0:
    user = input("Enter username: ")
    pw = input("Enter password: ")

    if user == username and pw == password:
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Incorrect login. Attempts left:", attempts)

if attempts == 0:
    print("Account locked")
