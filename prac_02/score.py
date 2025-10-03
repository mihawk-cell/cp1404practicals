"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

def main():
    """display grade"""
    score = get_score()
    grade = get_grade(score)
    print(grade)
    random_number = random.uniform(MINIMUM_SCORE, MAXIMUM_SCORE)
    #print(random_number)
    random_grade = get_grade(random_number)
    print(random_grade)

def get_grade(score):
    """Determine grade base on the score"""
    if score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASS_THRESHOLD:
        message = "Passable"
    else:
        message = "Bad"
    return message

def get_score():
    """Validate score"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

main()
