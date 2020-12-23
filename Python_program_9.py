#Write a program in Python to print all the numbers till 10 except 3, 7 using
#for and while loop

#using for loop
print("Using For loop :")
for i in range(0,11):
    if i==3 or i==7:
        continue
    print(i)

print("Using While loop")
#using while
i=-1
while i<10:
    i+=1
    if i==3 or i==7 :
        continue
    print(i)
   
