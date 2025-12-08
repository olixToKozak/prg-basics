# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.last_name=''
        self.age = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.last_name = 'Maxwell'
    student1.age = 19
    student2.name = "Olivia"
    student2.last_name = 'Rodrigez'
    student2.age = 21
    student3.name = 'Ahmed'
    student3.last_name =  'Ali'
    student3.age = 20

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name} {student1.last_name}, {student1.age} years old')
    print(f'{student2.name} {student2.last_name}, {student2.age} years old')
    print(f'{student3.name} {student3.last_name}, {student1.age} years old')

if __name__ == "__main__":
    main()