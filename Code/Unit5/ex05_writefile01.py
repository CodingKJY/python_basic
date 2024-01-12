def writeFile(filename):
    file   = open(filename, 'w')
    string = input('Write: ') + '\n'
    file.write(string)
    file.close()

testfile = 'write01.txt'
writeFile(testfile)