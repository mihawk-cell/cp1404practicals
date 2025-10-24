"""
Emails Program
Estimate: 20 minutes
Actual:
"""

def extract_name(email):
    """Extract the default name from the email"""
    # Get the part before @
    name_part = email.split("@")[0]
    # Replace a dot or underscore with a space
    name = " ".join(name_part.replace("_", " ").split("."))
    # Capitalize the first letter of each word
    return name.title()

# Use a dictionary to store emails and names
email_to_name = {}

while True:
    email = input("Email: ").strip()
    if email == "":
        break

    # Default name
    default_name = extract_name(email)

    # Confirm name
    response = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
    if response == "" or response == "y":
        name = default_name
    else:
        name = input("Name: ").strip()

    email_to_name[email] = name

# Print results
print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")
