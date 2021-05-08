items = input("Input comma separated sequence of words")
words = set(items.split(','))
print(",".join(sorted(list(words))))
