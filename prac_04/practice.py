def MAIN():
    REMOVE_NAMES()
    MISSING_FUNCTIONS()
    DYNAMIC_OUTPUT()

"""
Given a list of names, prompt the user to remove names until they enter an empty string.
Ensure the program does not crash when the name is not in the list.
"""

def REMOVE_NAMES():
    names = ["Ada", "Alan", "Bill", "John"]
    print(", ".join(names))
    name_to_remove = input("Who do you want to remove?").title()

    while name_to_remove != "":
        try:
            names.remove(name_to_remove)
        except ValueError:
            print("Name not in the list!")
        print(names)
        name_to_remove = input("Who do you want to remove? ").title()

"""
Teamwork: Write the missing functions

def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)
    
Example Output:
Enter numbers separated by commas: 1,4.5,2,90,-2,8,2
1.0..4.0..4.0..4.0..20.25..64.0..8100.0
"""

def MISSING_FUNCTIONS():
    def main():
        numbers = get_numbers()
        square_numbers(numbers)
        display_numbers(numbers)

    def get_numbers():
        text = input(f"Enter numbers separated by commas: ")
        numbers = text.split(',')
        return numbers

    def square_numbers(numbers):
        for i in range(len(numbers)):
            numbers[i] = float(numbers[i]) ** 2

    def display_numbers(numbers):
        print("..".join([str(number) for number in sorted(numbers)]))

    main()

"""
How do we get this dynamic neat output?

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

Desired output from any similar list of [name, score] pairs:

Derek       =   7
Xavier      =  80
Bob         = 612
Chantanelle =   9
"""

def DYNAMIC_OUTPUT():
    data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

    name_width = max((len(pair[0]) for pair in data))
    score_width = max((len(str(pair[1])) for pair in data))

    print(name_width)
    print(score_width)

    for pair in data:
        name, score = pair
        print(f"{name:{name_width}} = {score:{score_width}}")
    print()







MAIN()