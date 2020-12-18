#List
#let's first create demo list
numbers = [1,2,3,4,5,6,7,8,9,10]

#printing a list
print(numbers)

#method 1 : append(value)
# add new elements to the list
# can only add one element at a time
numbers.append(11)
print(numbers)

#method 2 : extend(values)
# add one or more than one element at a time
new = [12,13,14]
numbers.extend(new)
print(numbers)

#method 3 : insert(index,value)
#inserts spectific value to the index given
numbers.insert(0,0)
print(numbers)

#method 3 : sum(list)
#calculates the sum of all the elements of List
#this only sums the numeric values otherwise throw TypeError
print( sum(numbers) )

#method 4 : count()
#calculates total occurrence of given element of list
print( numbers.count(11) )


#method 5 : len(list)
#calculates total length of the list
print( len(numbers) ) 

#method 6 : index()
#Returns the index of first occurrence.
#Start and End index are not necessary parameters.
print( numbers.index(4) )

#method 7 : min()
#calculates minimun of the list
print( min(numbers) )

#method 8 : max()
#calculates maximum of the list
print( max(numbers) )
