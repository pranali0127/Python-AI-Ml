#importing prime function
import prime

n= int(input("enter dimention"))
print("enter a nXn matrix")
matrix=[] #to store NxN matrix
primes=[] #to store prime numbers
for i in range(0,n):
    exp =[]
    for i in range(0,n):
        e = int(input())
        if prime.isPrime(e):
            primes.append(e)
        exp.append(e)
    matrix.append(exp)

print("all prime numbers are : ")
print(*primes) #unpacking of a list
                   
        
