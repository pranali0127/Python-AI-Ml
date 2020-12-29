
#writing in a text file

with open("text_file1.txt","w") as f:
    f.write(" This are some quetions: \n")
    f.write('''Que1 :Write a program in Python which makes use of the Python error handling,
your program should include try, catch, raise keyword.
Que 2: Write a program in Python which makes use of the different match
functions(min 3) and the sort function for list, tuples, sets etc
Que3: Write a program in Python to read a text file and print it’s content. ''')

with open("text_file1.txt","r") as f:
    item = f.read()
    print(item)
    
