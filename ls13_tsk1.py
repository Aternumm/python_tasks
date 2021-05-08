def sum_items (*args):
    sum = 0
    for x in args:
        sum = sum +x
    return sum
def prod_items (*args):
    sum = 1
    for x in args:
        sum = sum * x
    return sum
print(sum_items (2, 4, 2))
print(sum_items (8, 6, 7, -5))
print(prod_items (2, 4, 2))

      
