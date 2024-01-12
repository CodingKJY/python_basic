def writeFile(filename):
    file   = open(filename, 'a')
    string = input('Write: ') + '\n'
    file.write(string)
    file.close()

testfile = './testfile/write02.txt'
writeFile(testfile)