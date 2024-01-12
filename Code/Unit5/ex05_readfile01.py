def readFile(filename, n = None):
    file = open(filename, 'r')
    print(file.read(n))
    file.close()

testfile = 'read.txt'
readFile(testfile)
readFile(testfile, 3)