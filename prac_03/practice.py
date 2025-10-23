s = "\tPython, Monty    \n"
print(s[1], ".", sep="")
print(s.strip(), ".", sep="")
s.replace(' ', '*')
print(s.lstrip(), ".", sep="")
print(s.strip().split(','))

name = input("Name: ")
# out_file = open("name.txt", "w")
# print(name, file=out_file)
with open("name.txt", "w") as out_file:
    print(name, file=out_file)

out_file.close()
print("Done")

names = ["Cliff", "Lucas", "Lea"]

for i in range(len(names)):
    with open(f"{names[i]}.txt", "w") as out_file:
        print(f"{names[i]}, file=out_file")

"""
Write code to read a file like this and print each data pair, like "Bob was born in NZ"

Bob\n
NZ\n
Jane\n
Myanmar\n
Derek\n
Australia\n
"""

with open("name.txt") as in_file:
    lines = in_file.readlines()

print(lines)

for i in range(0, len(lines), 2):
    print(lines[i].strip())
    print(lines[i+1].strip())
    name = lines[i].strip()
    country = lines[i+1].strip()
    print(f"{name} was born in {country}")

"""
Error kind:
TypeError
ValueError
ZeroDivisionError

"""




