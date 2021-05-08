def char_frequency(str1):
    dic = {}
    for n in str1:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    return dic
print(char_frequency('google.com'))
