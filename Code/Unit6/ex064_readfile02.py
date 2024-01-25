def readFile(filename, n = None, offset = 0):
    file = open(filename, 'r')
    file.seek(offset)
    print(file.read(n))
    file.close()

testfile = './testfile/read.txt'
readFile(testfile, 1, 0)
readFile(testfile, 1, 3)
readFile(testfile, 1, 6)