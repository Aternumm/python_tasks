x = input()
s = x.split()
max_item = s[0]
for item in s:
    if len(item) > len(max_item):
        max_item=item
print(max_item)
        
    
