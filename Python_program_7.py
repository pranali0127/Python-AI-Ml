#program 1

#function to return full name
def full_name(first_name,last_name):
    return '{} {}'.format(first_name,last_name)


#function to return total marks
def total_marks(marks):
    l = list(marks)
    return str(sum(l))
    

#function to return percentage on basis of marks
def per(total , n):
    per = total/n
    return str(per)

#function to return grade
def grade(score):
    if score>=95 :
        Grade = 'A'
    elif score>=85 and score<95 :
        Grade = 'B'
    elif score>=75 and score<85 :
        Grade = 'C'
    elif score>=65 and score<75 :
        Grade = 'D'
    return Grade 

#function to print all the details of a student
def details():
    marks = [98,90,78,89,88]
    first = "Pranali"
    last = "Mate"
    print( "Full name :",full_name(first,last) )
    print( "Marks :", *marks)
    print( "Total marks :",total_marks(marks) )
    total = int(total_marks(marks))
    n = len(marks)
    print( "Percentage :",per(total , n) )
    p = float(per(total,n))
    print( "Grade :",grade(p) )

details()
