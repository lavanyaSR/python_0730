class Student():
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.comp = self.computer()

    def show(self):
        print(self.name,self.id)
        self.comp.show()

    class computer():
        def __init__(self):
            self.brand = 'MAC'
            self.cpu = 'i5'
        def show(self):
            print(self.brand,self.cpu)


s1 = Student('Anya',12)
s2 = Student("Stef",34)
s1.show()
s2.show()

