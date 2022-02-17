# lists

# declaring a list
list1 = [1,2,3,4,5]
print(list1[2])
print(list1[4])

# printing a range of items in list
print(list1[2:4])
print(list1[1:])
print(list1[2:5])

# appending to a list
list1.append(7)
print(list1)

# change values in a list
list1[1] = 9
print(list1)

# deleting an element
del list1[4]
print(list1)

# finding length of a list
length = len(list1) 
print(length)

# adding two lists together
list2 = [10,13]
list3 = list2 + list1
print(list3)

# print list several times
replist = ["HELLO","WORLD"]
print(replist * 5)