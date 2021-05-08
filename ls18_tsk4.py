list1 = []
list2 = []
for x in range(1, 100):
    if x%3 == 0:
        list1.append(x)
    if x%5 == 0:
        list2.append(x)
set1 = set(list1)
set2 = set(list2)
print(set1&set2)
