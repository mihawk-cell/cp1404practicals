"""
a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100

b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

c. print a number of stars.
Ask the user for a number, then print that many stars (*), all on one line.

d. print lines of increasing stars.
Ask the user for a number of lines, then print lines of increasing stars, starting at 1 with no blank line.
"""

# ex.
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
star = int(input("Number of stars: "))

for i in range(star):
    print("*", end="")

print()

# d.
number_of_lines = int(input("Number of lines: "))

for i in range(1, number_of_lines + 1):
    print("*" * i)





