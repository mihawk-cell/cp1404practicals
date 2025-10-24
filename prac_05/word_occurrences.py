"""
Word Occurrences
Estimate: 20 minutes
Actual:
"""

# 1. Read user input
text = input("Enter a string: ")

# 2. Split text into words
words = text.split()

# 3. Count the number of times each word appears
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# 4. Find the longest word for output alignment
max_len = max(len(word) for word in counts)

# 5. Sort alphabetically and print
for word in sorted(counts):
    print(f"{word:{max_len}} : {counts[word]}")

