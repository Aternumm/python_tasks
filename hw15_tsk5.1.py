def rec(mylist, i=0):
    if i == len(mylist):
        return 1
    return mylist[i]*rec(mylist, i+1)
print(rec([2,3,4]))
