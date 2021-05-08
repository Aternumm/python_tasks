def findUnique(*arr):
    for x in arr:
       if arr.count(x) > 1:
           return False
    return True
print(findUnique(1,2,3,5))
       
