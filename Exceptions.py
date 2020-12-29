try: #it contains that lines of code who may cause error
    a=int(input("enter a"))
    b=int(input("enter b"))
    if b==0:
        raise ZeroDivisionError
    print("a/b =",a/b)

except ZeroDivisionError: #raise when user try to divide by zero
    print("Denominator should be greater than 0")

except TypeError: #raise when input is other than integer
    print("Division required two integers")

except Exception: #raise when other exception is occured
    print("An error occured")
    
