#Sets

#A Set is an unordered collection data type that
#is iterable, mutable and has no duplicate elements.
#it is represents as { }

#lets first create some sets

s1={1,2,3,4,5}
s2={4,5,6,7}

print("s1 :",s1)
print("s2 :",s2) 
# Set methods

#method 1 : add()
#Adds an element to the set
s2.add(8)
print(s2)

#method 2: clear()
#remove all the element from the list
s3={10,20,30}
print("s3 :",s3)
s3.clear()
print("s3 :",s3)

#method 3: union()
#Return a set containing the union of sets.
s3 = s1.union(s2)
print("Union of s1 & s2 :",s3)

#method 4 : intersection()
#returns a set , that is the intersection of both the sets.
s3 = s1.intersection(s2)
print("Intersection of s1 & s2 :",s3)

#method 5 : difference()
#returns a set containing the difference between two or more sets
s3 = s1.difference(s2)
print("Difference of s1 & s2 (s1 - s2 ) :",s3)

s3 = s2.difference(s1)
print("Difference of s2 & s1 (s2 - s1 ) :",s3)

#method 6 : pop()
#removes an element from the set
s2.pop()
print("poped from s2 :",s2)

#method 7 : issubset()
#returns whether another set contains this set or not
s3 = {1,2,3}
print("s3 :",s3)
print("is s3 subset of s1? :",s3.issubset(s1) )

#method 8 : issuperset()
#returns whether this set contains another set of not.
print("is s1 supersset of s3? :",s1.issuperset(s3))
