# polymorphism in python 4 types
# Duck typing, operator overloading, method overloading, method overriding

class PyCharm:
    def execute(self):
        print("Running")
        print("Compiling")

class MyEditor:
    def execute(self):
        print("Running")
        print("Compiling")
        print("spell check")
class Laptop():
    def code(self,ide):
        ide.execute()

#even though if you change also it will work as both classes has same method which is execute()
#ide = PyCharm()
ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

#Method overloading - addition and subtraction and other arthmetic ope has methods to add/sub but for classes
#there is no method available to add 2 classes..so we will overload method __add__ here

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3

s1 = Student(45,67)
s2 = Student(78,98)
s3 = s1+s2
print(s3.m1)

#method overloading and method overriding
class Stu:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a = None, b = None, c = None):
        if a!=None and b!= None and c!= None:
            s = a+b+c
        elif a!= None and b!= None:
            s = a+b
        else:
            s = a
        return s
s1 = Stu(56,89)
print(s1.sum(2,3,6))

#method overriding -
class A:
    def show(self):
        print("in show A")
#when no method and pass it used parent class method and prints in show A
class B(A):
    #pass
    def show(self):
        print("in show B")  # it shows B method as it has its own method

a = B()
a.show()

