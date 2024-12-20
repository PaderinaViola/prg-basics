# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.gender = "Male"
    student2.name = "Olivia"
    student2.age = 21
    student2.gender = "Male"
    student3.name = "Solomiia"
    student3.age = 17
    student3.gender = "Female"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student3.gender}')
    print(f'{student2.name}, {student2.age} years old, {student2.gender}')
    print(f'{student3.name}, {student3.age} years old, {student3.gender}')

if __name__ == "__main__":
    main()