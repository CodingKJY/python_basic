def readFile(filename, offset = 0):
    file = open(filename, 'r')
    file.seek(offset)
    print(file.readline())
    file.close()

testfile = 'read.txt'
readFile(testfile, 0)
readFile(testfile, 3)
readFile(testfile, 6)