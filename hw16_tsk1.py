def read_file(filename):
    file = open(filename,"r")
    for line in file:
        print(line, end="")
    file.close()

read_file('C:\\Python.txt')
