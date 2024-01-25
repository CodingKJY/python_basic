# Unit 6: File I/O
[↩️ back to menu](../../README.md)

There are four basic operation of file handling:
- Open 
- Read
- Write
- Close

To handle a file, we use `open(FilePath, mode)` to obtain a file object. After that, we can use reading and writing methods

```python
file = open(FilePath, mode)
# do something
file.close()
```
> Notice: `open()` must be used with `close()`

|Mode |Description|
|:---:|:----------|
|`'r'`|open for reading only, failing if the file not exists (Default)|
|`'w'`|open for writing only, turncating the file first|
|`'a'`|open for writing only, appending to the end of the file if it exists|
|`'x'`|open for writing only, failing if the file already exists|
|`'b'`|binary mode|
|`'+'`|open for updating (reading and writing)|
- r/w/a/x cannot be used at the same time
- `'r+'` -> read and write mode, failing if the file not exists
- `'rb'` -> binary read only mode
- `'w+'` -> write and read mode

## File Methods
|Method|Description|
|:-----|:----------|
|`seek(offset)`|move file pointer with offset|
|`tell()`|return the current file pointer's position|

## Read/Write Methods
|Method|Description|
|:-----|:----------|
|`read(size)`|return size-bit of file start from the file pointer|
|`readline()`|return a line of file start from the file pointer|
|`readlines()`|return a list of strings (lines) start from  the file pointer|
|`write(string)`|write string to the file after the file pointer|
|`writelines(stringList)`|write a list of strings to the file after the file pointer|

## A simple file handling method implementation
In python, `with` statement is a simple way to handle execptions. We can use `with` to implement file handling methods
We have the following methods:
- `newFile(filePath, data)` | create a new file, and write initial data
- `updateFile(filePath, data)` | appending data to a file
- `readFile(filePath)` | return file data as a list of string

```python
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
```