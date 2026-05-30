MINIMUM_LENGTH = 5
password = input("Enter password: ")
while len(password) < MINIMUM_LENGTH:
    print("Your password is too short")
    password = input("Enter password: ")

print("*" * len(password))