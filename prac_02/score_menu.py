MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
MENU = "(G)et a valid score \n(P)rint result \n(S)how starts \n(Q)uit"

def main():
    """Displaying main menu"""
    student_score = -1

    print(MENU)
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "G":
            student_score = get_score()
        elif choice == "P":
            student_score = Validate_score(student_score)
            print(get_grade(student_score))
        elif choice == "S":
            student_score = Validate_score(student_score)
            display_stars(student_score)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input("Enter choice: ").upper()

    print("Farewell")

def Validate_score(student_score):
    """Check if user enter score"""
    if student_score == -1:
        student_score = get_score()
    return student_score

def display_stars(student_score):
    """Display starts"""
    print(int(student_score) * "*")

def get_score():
    """Validate score"""
    student_score = float(input("Enter score: "))
    while student_score < MINIMUM_SCORE or student_score > MAXIMUM_SCORE:
        print("Invalid score")
        student_score = float(input("Enter score: "))
    return student_score

def get_grade(score):
    """Determine grade base on the score"""
    if score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASS_THRESHOLD:
        message = "Passable"
    else:
        message = "Bad"
    return message

main()
