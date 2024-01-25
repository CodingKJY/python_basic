class Human:
    def __init__(self, age, height, weight) -> None:
        self.__age    = age
        self.__height = height
        self.__weight = weight
    
    def __str__(self) -> str:
        age    = f'Age   : {self.__age}\n'
        height = f'Height: {self.__height}\n'
        weight = f'Weight: {self.__weight}'
        return '<Private Data>\n' + age + height + weight

class Student(Human):
    def __init__(self, studentID, name, age, height, weight) -> None:
        super().__init__(age, height, weight)
        self.name      = name
        self.studentID = studentID
    
    def __str__(self) -> str:
        name      = f'Name     : {self.name}\n'
        studentID = f'StudentID: {self.studentID}\n'

        return '<Open Data>\n' + studentID + name + super().__str__()
    
std1 = Student('1130114', 'Tim', 22, 170.4, 66.3)
print(std1)