#creating function who check if given number is prime or not
def isPrime(num):
    if num > 1:
        if num==2:
            return True
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
            else:
                return True
 
    else:
        return False
