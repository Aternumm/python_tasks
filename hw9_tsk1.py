x = [0, 5, 2, 4, 7, 1, 3, 19]
count = 0
for i in x:
    if i%2 != 0:
        count += 1
print (count, len(x) -  count)

