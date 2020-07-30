#declaring a class
class Car():
    def __init__(self,modelname,price,mileage):
        self.modelname = modelname
        self.price = price
        self.mileage = mileage
    def price_inc(self):
            self.price  = int(self.price * 1.5)

honda = Car('Civic',20000,35)
Tesla = Car('X',35000,80)

honda.cc = 1500

print(honda.__dict__)
print("Tesla model ",Tesla.__dict__)

print("Tesla price", Tesla.price)
Tesla.price_inc()
print("Tesla price", Tesla.price)


class Computer():
    def __init__(self,cpu,memory):
        self.cpu = cpu
        self.memory = memory
    def config(self):
        print("config is ",self.cpu,self.memory)

com1 = Computer('250GB',500)
com2 = Computer('120GB',250)

com1.config()
com2.config()

class Comp():
    def __init__(self):
        self.name = 'Anya'
        self.age = 38

    def update(self):
        self.age = 50
c1 = Comp()
c2 = Comp()
c1.name = "Tanya"
c1.age = 45
print(c1.name,c1.age)
print(c2.name,c2.age)
c1.update()
print(c1.age)

print()
print()
print()

# types of variables: class/static instance variables
class Car1():
    #class variable / static variable
    wheels = 4
    def __init__(self):
        #instance variable
        self.mil = 30
        self.comp = 'BMW'

c1 = Car1()
c2 = Car1()
c1.mil = 20
#to change class variable
Car1.wheels = 5
print(c1.mil,c1.comp,c1.wheels)
print(c2.mil,c2.comp,c2.wheels)

#types of methods: Class method, static method, instance method
class Student:
    school = "Stanford"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    #to access class variable we are using class method
    @classmethod
    def getSchool(cls):
        return cls.school

    #static method - not related to class/ instance methods
    @staticmethod
    def info():
        print("this is just static method")
        print("can be used to show pi value or fact of a number which is not related")


s1 = Student(45,56,68)
s2 = Student(67,78,89)
print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()

