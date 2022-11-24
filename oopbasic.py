class Student:
    
    def __init__(self):
        self.grade="11"
        self.age="16"
        self.faculty="mgmt"
    
    def getDetail(self, grade, age, faculty): 
        self.grade= grade
        self.age = age
        self.faculty = faculty
            
    def showDetail(self):
        print(f"age is {self.age}")
        print(f"grade is {self.grade}")
        print(f"faculty is {self.faculty}")

a = 1
while(a==1):
    name = input("enter name: ")
    name = Student()
    grade = input("Enter grade: ")
    age = input("Enter age: ")
    faculty = input("Enter faculty: ")
    name.getDetail(grade, age, faculty)
    a = int(input("enter choice: "))
    if(a==0):
        name1=input("Enter name: ")
        name1.showDetail()
