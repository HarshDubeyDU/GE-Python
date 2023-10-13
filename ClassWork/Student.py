class Student:
    def __init__(self, name, age, rollNo):
        self.name = name
        self.age = age
        self.rollNo = rollNo

    def introduce(self):
        print(f"Hi I'm {self.name}, I am {self.age} years old and my Roll No is {self.rollNo}")


student1 = Student("Arif", 18, 20232731)
student1.introduce()
