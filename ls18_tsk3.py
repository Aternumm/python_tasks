text1 = input()
text2 = input()
words1 = text1.split()
words2 = text2.split()
set1 = set(words1)
set2 = set(words2)
print(set1 & set2)