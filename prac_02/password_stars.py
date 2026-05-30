MINIMUM_LENGTH = 5

def main():
    password = get_password()

    display_asterisks(password)


def display_asterisks(password):
    print("*" * len(password))


def get_password() -> str:
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Your password is too short")
        password = input("Enter password: ")
    return password


main()