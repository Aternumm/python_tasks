x = {}
s = "one two two tree tree tree"
s = s.split()
for item in s:
    if item in x:
        x[item]+=1
    else:
        x[item]=1
print(x)
for item in x:
    if x[item]==1:
        print(item)
