#this is main program which call every program
#first import all the programs
import program1 as p1
import program2 as p2
import program3 as p3

#program1 functions

#function to return square of number
n= int(input("enter number"))
print("square of number :",p1.square(n) )


n = int(input("enter dimention"))                                # for size
#l = list(map(int, input().split()[:n]))  # to input n elements
l=[]
for i in range(n):
    l.append(int(input()))
print(l)

#function to return max of list
print("max :", p1.max_from_list(l) )

#function to print min of list
print("min:",p1.min_from_list(l) )

#function to print sum of list
print("sum:",p1.sum_of_list(l) )

#program2 functions

string = input("enter string")

#function to return middle element of string
print("middle of string: ",p2.middle(string) )

#function to count vowels in string
print("count of vowels :",p2.count_vowel(string) )

#function to calculate length of string
print("length of string :",p2.length(string) )

#function to count words of string
print("number of words: ",p2.words_count(string) )

#program3 functions

#AND operator

p3.and_operator()
p3.or_operator()
p3.not_operator()



