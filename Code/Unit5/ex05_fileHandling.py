def newFile(filePath, data = None):
    with open(filePath, 'w') as file:
        file.write(data)

def updateFile(filePath, data):
    with open(filePath, 'a') as file:
        file.write(data)

def readFile(filePath):
    data = []
    with open(filePath, 'r') as file:
        data = file.readlines()
    return data

filename  = 'test.txt'
init_data = 'initial data\n'
append_data = 'append data\n'

newFile(filename, init_data)
updateFile(filename, append_data)
print(readFile(filename))