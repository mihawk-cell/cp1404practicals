"""
Hex Colours Lookup
Estimate: 15 minutes
Actual:
"""

COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

while True:
    name = input("Enter a colour name (blank to stop): ").strip().lower()
    if name == "":
        print("Program stopped.")
        break
    if name in COLOURS:
        print(f"The hex code for {name} is {COLOURS[name]}")
    else:
        print("Invalid colour name, please try again.")
