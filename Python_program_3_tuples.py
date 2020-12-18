#Tuples

#Tuples are similar to list but this are immutable means we cannot change values.
#this are represent as ( )

#first let's create demo tuple

numbers = (1,2,3,4,5,6,7,8,9)
print(numbers)

#Tuples can also created without paranthesis
num = 10,20,30
print("num =",num)

#Accessing values in tuple
print(numbers[4])

#deleting a tuple
del num
print("Deleted")

#Tuples method

#method 1 : count()
#counts the occurrence of element
print( numbers.count(2) )

#method 2 : index()
#returns the index of element
print( numbers.index(5) )

#method 3 : len(tuple)
#calculates total length of the tuple
print( len(numbers) ) 
