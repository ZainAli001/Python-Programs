# Exercise 1: Calculate the multiplication and sum of two numbers
a,b =20,30
if a*b <= 1000:
    print(f"Result = {a*b}")
else:
    print(f"Result = {a+b}")
# -------------------------------------------

# Exercise 2: Print the sum of the current number and the previous number

for i in range(1,11):
    print(f"Current Number {i} Previous Number {i-1} sum = {i+(i-1)}")
# -------------------------------------------
# Exercise 3: Print characters from a string that are present at an even index number
string = "pynative"

for i in range(len(string)):
 
    if i % 2==0:
        print(string[i])
    
# ------------------------------------------

# Exercise 4: Remove first n characters from a string

def remove_char(string ,num):
    return string[num:]

string= input("Enter string :")
num= int(input("How many characters do you wanna remove :"))
obj =remove_char(string,num)
print(obj)
# ----------------------------------------
# Exercise 5: Check if the first and last number of a list is the same

def first_last_check(list=[]):
    if list[0] == list[-1]:
        return True
    else:
        return False
    
obj = first_last_check([10, 20, 30, 40, 10])
print(obj)

# ----------------------------------------
# Exercise 6: Display numbers divisible by 5 from a list
list1 = [10, 20, 33, 46, 55]
x = [x for x in list1 if x%5==0]
print(x)

# -------------------------------------------
# Exercise 7: Return the count of a given substring from a string. Write a program to find how many times substring “Emma” appears in the given string.
str_x = "Emma is good developer. Emma is a writer"
sum_=0
for i in str_x.split(" "):
    if i =="Emma":
        sum_+=1
print(f"Emma appeared {sum_} times")  


# -----------------------------------------
# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

for i in range(1,6):
    for x in range(i):
        print(i,end=" ")
    print()

# ---------------------------------------
# Exercise 9: Check Palindrome Number
number = input("Enter number =")

if number[0] == number[-1]:
    print("Yes. given number is palindrome number")
else:
    print("No. given number is palindrome number")

# ------------------------------------------
# Exercise 10: Create a new list from a two list using the following condition
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_list1 = [x for x in list1 if x%2 !=0]
print(new_list1)
new_list2 = [x for x in list2 if x%2 ==0]

result = list(zip(new_list1,new_list2))
print(result)
# ------------------------------------------
# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
number = 7536
x = str(number)
print(x[::-1],sep="\t")

# ------------------------------------------
# Exercise 13: Print multiplication table form 1 to 10

for i in range(1,11):
    for x in range(1,11):
        print(i*x,end=" ")
    print("\t\t")
# ------------------------------------------
# Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

for i in range(6,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print()
# ------------------------------------------

# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
    
def exponent(base,exp):
    return base**exp

obj = exponent(2,5)
print(obj)