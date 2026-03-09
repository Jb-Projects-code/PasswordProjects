import random
import string

length = int(input("Enter Password Length: "))
charecters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(charecters) for i in range (length))
print("Generated password", password)
