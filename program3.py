#this shows all the logical operator

def and_operator():
    print("AND operator returns true if both the operands are true otherwise false.")
    print("Example:")
    num = 10
    print("num=",num)
    print( "num>1 and num%5==0 :", num>1 and num%5==0 )
    print( "num>1 and num%5!=0 :",num>1 and num%5!=0 )

def or_operator():
    print("OR operator returns true if one of the operands are true otherwise false.")
    print("Example:")
    num = 10
    print("num=",num)
    print(" num>0 or num%5==0 : ",num>0 or num%5==0 )
    print( " num>0 or num%5!=0 :",num>0 or num%5!=0 )

def not_operator():
    print("NOT operator do exact opposite to given ")
    print("it return true to false and false to true")
    print("Example:")
    num=10
    print("num=",num)
    print("not(num==10) :",not(num==10))
    print("not(num>1 and num%5==0) :",not(num>1 and num%5==0))
    print("not(num>0 or num%5!=0) :",not(num>0 or num%5!=0))
    
    
