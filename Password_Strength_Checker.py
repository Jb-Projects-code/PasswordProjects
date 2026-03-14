import string

password = input("Password: ")

score = 0 

#check for the length
if len(password) >= 8: 
    score += 1

#check for lowercase
if any(char.islower() for char in password):
    score += 1

#check for upper#
if any(char.isupper() for char in password):
    score += 1

#check for digits
if any(char.isdigit() for char in password):
    score +=1

#check for special digits
if any(char is string.punctuation for char in password):
    score += 1 

#strength rating
if score >= 5:
    print("password strength: strong")

elif score >= 3:
    print("password strength: medium")

elif score >3: 
    print("Password strength: weak") 

elif score >= 2:
    print("Hackers must love you")
