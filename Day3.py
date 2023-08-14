# Exercise 1: Print First 10 natural numbers using while loop
natural_num = [x for x in range(1,11)]
print(natural_num)
# --------------------------------------------------
# Exercise 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# --------------------------------------------------
# Exercise 3: Calculate the sum of all numbers from 1 to a given number
import functools
num = int(input("Enter number ="))
sum_ = functools.reduce(lambda a,b:a+b,[x for x in range(1,num+1)])
print(sum_)
# --------------------------------------------------
# Exercise 4: Write a program to print multiplication table of a given number
num = int(input("Enter number ="))
for i in range(1,11):
    print(i*num)
# --------------------------------------------------
# Exercise 5: Display numbers from a list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)
# --------------------------------------------------
# Exercise 6: Count the total number of digits in a number
num = 75869
nums = len(list(map(int,[x for x in str(num)])))
print(nums)
# --------------------------------------------------
# Exercise 7: Print the following pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
# --------------------------------------------------
# Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in list1[::-1]:
    print(i)

# --------------------------------------------------
# Exercise 9: Display numbers from -10 to -1 using for loop
for i in range(-10,0,1):
    print(i)
# --------------------------------------------------
# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done")
# --------------------------------------------------
# Exercise 11: Write a program to display all prime numbers within a range
start = 25
end = 50
for num in range(start,end+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)

# --------------------------------------------------
# Exercise 12: Display Fibonacci series up to 10 terms
a = 0
b = 1
fab_num = int(input("Enter number :"))
for i in range(fab_num):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
# --------------------------------------------------
# Exercise 13: Find the factorial of a given number
num =5
sum_=1
for i in range(num,0,-1):
    sum_ = sum_*i 
print(sum_)
  

# --------------------------------------------------
# Exercise 14: Reverse a given integer number
num=76542
nums = list(map(str,[x for x in str(num)]))
print("".join(nums[::-1]))
# --------------------------------------------------
# Exercise 15: Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1,len(my_list)+1):
    if i %2 != 0:
        print(my_list[i],end=" ")
# --------------------------------------------------
# Exercise 16: Calculate the cube of all numbers from 1 to a given number

num  = 6
for i in range(1,num+1):
    # print(i**3,end=" ")
    print(pow(i,3),end=" ")
# --------------------------------------------------
# Exercise 17: Find the sum of the series upto n terms
n = 5
start = "2"
list1= []
for i in range(1,n+1):
    i = start
    list1.append(i)
    start += "2"
totla_sum  = sum(list(map(int,list1)))
print(totla_sum)

# --------------------------------------------------
# Exercise 18: Print the following pattern

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end= " ")
    print()
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end= " ")
    print()