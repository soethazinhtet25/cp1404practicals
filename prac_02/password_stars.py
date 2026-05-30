MINIMUM_LENGTH = 5

def main():
    """Password checking program."""
    password = get_password()

    display_asterisks(password)


def display_asterisks(password):
    """Display asterisks based on the length of the password."""
    print("*" * len(password))


def get_password() -> str:
    """Determine if the password is valid."""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Your password is too short")
        password = input("Enter password: ")
    return password


main()