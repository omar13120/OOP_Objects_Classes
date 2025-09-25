#first subtask
class Student:
    school = "AI University"
    studentCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.studentCount += 1
    
    def printStudent(self):
        print(f"Name: {self.name}, age: {self.age}, school: {self.school}")

    def getStudentCount():
        return Student.studentCount

#second subtask
s1 = Student("Ali", 21)
s2 = Student("Sara", 22)

s1.printStudent()
s2.printStudent()

print("Yes" if s1.school == s2.school else "No")

#third subtask
s1.age = 23
print(s1.age, s2.age, sep=" ") #s2's age didn't change

#fourth subtask
Student.school = "Tech Academy"
print(s1.school, s2.school, sep = ", ") #the schools changed!

#fifth subtask
print(Student.getStudentCount()) # if you make the first part the class name, it would belong to the whole class.

#final review
#class instances rely on self, and they're objects
#but class variables are global within the class

#Yes, It is by doing ClassName.var = x for example

#One, I think

