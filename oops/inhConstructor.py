class A():
    def __init__(self):
        print("init A method")
    def feature1(self):
        print("inside feature1")
    def feature2(self):
        print("inside feature 2")

#class B inherits class A and all methods comes under B - here B is single level inheritence
# class B(A):
#     def __init__(self):
#         print("init B method")
#         #super() is used to call super class constructor
#         super().__init__()
#     def feature3(self):
#         print("inside feature1")
#     def feature4(self):
#         print("inside feature 2")

class B:
    def __init__(self):
        print("init B method")
    def feature3(self):
        print("inside feature1")
    def feature4(self):
        print("inside feature 2")

# if define class C and inherits from A and B as its
# connected first to A, will take init from A when mentioned super. MRO (method resolution order)
class C(A,B):
    def __init__(self):
        print("inside C")
        super().__init__()

    def feat(self):
        super().feature1()

a1 = C()
a1.feat()
