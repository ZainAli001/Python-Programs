'''Tuple Excersice'''
# Exercise 1: Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
print(tuple(reversed(tuple1)))

#------------------------------------------------------
# Exercise 2: Access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
#------------------------------------------------------
# Exercise 3: Create a tuple with single item 50
tuple1 = (50,)
print(tuple1)
#------------------------------------------------------
# Exercise 4: Unpack the tuple into 4 variables
tuple1 = (10, 20, 30, 40)

a, b, c, d = tuple1
print(a,b,c,d)
#------------------------------------------------------
# Exercise 5: Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)
#------------------------------------------------------
# Exercise 6: Copy specific elements from one tuple to a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
new_tuple = tuple1[3:5]
print(new_tuple)
#------------------------------------------------------
# Exercise 7: Modify the tuple
tuple1 = (11, [22, 33], 44, 55)
new_tuple = tuple1
new_tuple[1][0] = 222
print(tuple(new_tuple))
#------------------------------------------------------
# Exercise 8: Sort a tuple of tuples by 2nd item 
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
x=tuple(sorted(list(tuple1),key=lambda x:x[1]))
print(x)
#------------------------------------------------------
# Exercise 9: Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))
#------------------------------------------------------
# Exercise 10: Check if all items in the tuple are the same 

tuple1 = (45, 45, 45, 45)

if tuple1.count(tuple1[0]) == len(tuple1): 
    print(True)
else:
    print(False)
