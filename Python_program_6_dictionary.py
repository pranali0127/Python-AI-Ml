#Dictionary

#Each key is separated from its value by a colon (:),
#the items are separated by commas, and the whole thing is enclosed in curly braces
#An empty dictionary without any items is written with just two curly braces, like this: {}.
#Keys are unique within a dictionary while values may not be.

#lets create demo dictinary
dict = {1:"red" , 2:"blue" , 3:"orange" , 4:"purple" , 5:"black"}
print("dict :",dict)

# Dictinary method

#method 1 : clear()
#removes all elements from dictionary
d = {"one" :1,"two":2}
print("d :",d)
d.clear()
print("dictonary d cleared \nd=",d)

#method 2 : copy()
#returns a shallow copy of dictionary dict
d = dict.copy()
print("copy of dict :",d)

#method 3 :get()
#return value of provided key
print( dict.get(4) )

#method 4 :has_key()
#returns true if key in dictinary dict, false otherwise
print( "is key 5 present in dict? :",dict.has_key(5))
print( "is key 7 present in dict? :",dict.has_key(7))

#method 5 : items()
#Returns a list of dict's (key, value) tuple pairs
print( dict.items() )

#method 6 : keys()
#Returns list of dictionary dict's keys
print( dict.keys() )

#method 7 : values()
#Returns list of dictionary dict's values
print( dict.values() )
