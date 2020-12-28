def middle(string):
    index = len(string)//2
    return string[index]

def count_vowel(string):
    vowels = ['a' ,'e','i','o','u']
    c=0
    for i in string:
        if i in vowels:
            c+=1
    return c

def length(string):

    #return len(string)
    #by using bild in function
    #but we use manual method
    c=0
    for i in string:
        c+=1
    return c

def words_count(string):
    
    string=string.split()
    return len(string)

