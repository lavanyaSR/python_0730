class A():
    def feature1(self):
        print("inside feature1")
    def feature2(self):
        print("inside feature 2")
#class B inherits class A and all methods comes under B - here B is single level inheritence
class B(A):
    def feature3(self):
        print("inside feature1")
    def feature4(self):
        print("inside feature 2")
#multi level, here C will inherit from both A and B
class C(B):
    def feature5(self):
        print("inside feature1")
    def feature6(self):
        print("inside feature 2")

#multiple level
class D(A,B):
    def feature7(self):
        print("inside feature 2")

a1 = A()
a1.feature2()
b1 = B()
b1.feature1()
c1 = C()
c1.feature1()
