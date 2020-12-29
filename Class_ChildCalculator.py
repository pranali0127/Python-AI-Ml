class calculator:
    def __init__(self,i1,i2):
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
obj1 = calculator(a,b)
obj1.display()
print( "a+b:",obj1.add() )
print( "a-b:",obj1.subtract() )
print( "a*b:",obj1.multiply() )
print( "a/b:",obj1.divide() )


class ChildCalculator(calculator): #inherited the calculator class
    def add(self):
        result = super().add()
        print( "Result of adding",self.input1,"and",self.input2,"is",result)

    def subtract(self):
        result = super().subtract()
        print( "Result of subtracting",self.input1,"and",self.input2,"is",result)
        
obj2 = ChildCalculator(a,b)
obj2.add()
obj2.subtract()
        
    
