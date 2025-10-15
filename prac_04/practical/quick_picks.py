import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    count = int(input("How many quick picks? "))
    for i in range(count):
        pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in pick))

def generate_quick_pick():
    pick = []
    while len(pick) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in pick:
            pick.append(num)
    pick.sort()
    return pick

main()
