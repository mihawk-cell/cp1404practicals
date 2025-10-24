"""
Word Occurrences
Estimate: 20 minutes
Actual:
"""

# user input
text = input("Enter a string: ")

# text split to words
words = text.split()

# Counting occurrences using a dictionary
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Find the longest word and use it to format the output
max_len = max(len(word) for word in counts)

# Sort alphabetically and print
for word in sorted(counts):
    print(f"{word:{max_len}} : {counts[word]}")
