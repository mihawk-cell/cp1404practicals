# Setting minimum length of password
MIN_LENGTH = 6

# Keep asking for input until the conditions are met
while True:
    password = input("Enter password :".format(MIN_LENGTH))
    if len(password) >= MIN_LENGTH:
        break

# Output asterisks with the same length as the passwords
print("*" * len(password))


