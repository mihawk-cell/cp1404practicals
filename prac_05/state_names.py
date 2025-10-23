"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

for code, name in STATE_NAMES.items():
    print(f"{code:3} is {name}")

print()

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(STATE_NAMES[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
