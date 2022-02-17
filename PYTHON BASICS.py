# PYTHON IN 60 MIN
# PYTHON BASICS IN 9 SUB TOPICS
# 1.COMMENT
# This is a comment 
# we will write comment in the form of # starting in python
# whereas in  c we will write // or /* */
# 2.DATATYPES
# Data types in .py integers,strings,booleans,float/real
# integers - whole numbers
# strings - characters , symbols written in the form of ""
# boolean - true or false statements 
# float/real :- decimal numbers (1.2,4.5)
# 3.PRINT
print (1)
print("this is my first .py ")
print(True)
print(False)
print(3.4)
# 4.VARIABLES
age = 28 #storing integer
name = "jack" #storing a string
print(age)
print(name)
# 5.NUMBERS
x =50
y =10
sum = x + y
print(sum)
# Sub parts in numbers
#similarly perform sub multi and divi
#now lets do something new 
# floor Division = dividing and rounding down to the nearest integer
w = 2
z = 3
print (z//w)
# Remainders 
print (z%w)
# Powers 
print (2**3)
# 6.Comparsion operators
# greater than(>), less than(<),(>=),(<=),(==),(!=)
print(2>3)
print(2<3)
print(2>=2)
print(3<=6)
print(1!=4)
print() # Will print blank space 
g =3
d =5
print(g>d)
#7.Lists
# Declaring a list 
list1 = [1,2,3,4,5] # numbers in list are stored in the form of index which starts with 0
print(list1)
print(list1[2])
# Printing a range of items in the list
print(list1[1:5])
# Appending to a list
list1.append(6) # adds the number to the list
print(list1)
# Change values in a list
list1[0] = 0
print(list1)
# Deleting on element 
del list1[4] # to delete the element in list("remeber the 4 is the number of index where index starts from 0")
print (list1)
# Finding the length of lisit
length = len(list1) 
print(len(list1)) # if we write above step we can write simple as print (length)
# Adding two lists together 
list2 =[1,6]
list3 = list1 + list2
print(list3)
# Print list several times 
replist = ["hello","world"]
print(replist *4)
# 8.If,Elif,Else
age =int(input("Enter your age:"))
if age >18:
  print("your are adult")
elif age <18: 
 print("you are young")
else:
 print("you are 18!")
# 9. Functions 
def main ():
    print("This is the main function")
main() # mandatory to run above function
# Need to learn more about functions 
# Bye 
# See you soon.....!
