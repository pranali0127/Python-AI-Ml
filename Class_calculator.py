#created class calculator
class calculator:
    def __init__(self,i1,i2): #constructor
        self.input1=i1
        self.input2=i2

    def add(self):
        return self.input1 + self.input2

    def subtract(self):
        return self.input1 - self.input2

    def multiply(self):
        return self.input1 * self.input2

    def divide(self):
        return self.input1 / self.input2

    def display(self):
        return "input1: {} , input2: {}".format(self.input1,self.input2)

a = int(input("enter input1 :"))
b = int(input("enter input2 :"))
obj1 = calculator(a,b) #object of class calculator
obj1.display()
print( "a+b:",obj1.add() )
print( "a-b:",obj1.subtract() )
print( "a*b:",obj1.multiply() )
print( "a/b:",obj1.divide() )
