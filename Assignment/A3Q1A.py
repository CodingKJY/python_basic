class Student:
    def __init__(self, studentID, studentName, studentAge, studentProg):
        self.sID   = studentID
        self.sName = studentName
        self.sAge  = studentAge
        self.sProg = studentProg

    def __str__(self) -> str:
        return f'SID: {self.sID}, Name: {self.sName}, Age: {self.sAge}, Prog: {self.sProg}'

def main():
    studentRep = []
    while True:
        action = input("Input 'A' to add record, 'D' to delete record, 'P' to print all records, 'q' to quit: ")
        if action == 'A': 
            sID   = input("Input student ID: ")
            sName = input("Input student name: ")
            sAge  = input("Input student age: ")
            sProg = input("Input student programme: ")
            sRecord = Student(sID, sName, sAge, sProg)
            studentRep.append(sRecord)
            print('')
            
        elif action == 'D': 
            targetID  = input('Provide Student ID to Delete Record: ')
            for student in studentRep: 
                if(student.sID == targetID):
                    studentRep.remove(student)
                    isDeleted = True
                    break
            if isDeleted: print(f'Student ID {targetID} Record Has Been Deleted.')
            else: print(f'Studnet ID {targetID} not found')
            print('')

        elif action == 'P': 
            print(f'Number of Studnet Representative(s): {len(studentRep)}')
            for student in studentRep:
                print(student)
            print()

        elif action == 'q': break
        else: print('Wrong Input\n')

    print("***  EDN of Program ***")

if __name__ == "__main__":
    main()
