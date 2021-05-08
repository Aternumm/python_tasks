def words_count(filename):
    file = open(filename, "rt")
    data = file.read()
    words = data.split()
    file.close()
    return len(words)
filename = "C:\\Python.txt"
print('Количество слов: ', words_count(filename))
