# create list
l = [11,54,76,34,23,55,98,9,90,78,10]
print("List :",l)
sorted_list = sorted(l)
print("Sorted list using sorted function : ",sorted_list )
l.sort()
print("Sorted list using sort function :",l  )

#created tuple
t = (11,54,76,34,23,55,98,9,90,78,10)
#t.sort() tuple does not have inbuild function to sort
print("Tuple :",t)
s_t = sorted(t , reverse =True)
print("sorted tuple (Desc ):",s_t)
s_t1 = sorted(t , reverse =False)
print("sorted tuple (ASC) :",s_t1)

