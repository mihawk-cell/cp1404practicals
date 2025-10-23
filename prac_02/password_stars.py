MIN_LENGTH = 6
# Setting minimum length of password
def main():
# Keep asking for input until the conditions are met
    password = get_password()
    # Output asterisks with the same length as the passwords
    print_asterisks(password)

def print_asterisks(password):
    print("*" * len(password))

def get_password():
    while True:
        password = input("Enter password :".format(MIN_LENGTH))
        if len(password) >= MIN_LENGTH:
            return password

main()


