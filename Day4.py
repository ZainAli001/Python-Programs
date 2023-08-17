# Write a program to create a new string made of an input string’s first, middle, and last character for odd len names.
# name = input("Enter Name =")
# first = name[0]
# middle = name[int(len(name) / 2)]
# last = name[-1]
# print(first,middle,last,sep="")
# ---------------------------------------------------
# Write a program to create a new string made of the middle three characters of an input string.
# str1 = "JhonDipPeta"
# str1 = "JaSonAy"
# middle = str1[int(len(str1) / 2)]
# x = str1.index(middle)
# print(str1[x-1],middle,str1[x+1],sep="")
# ---------------------------------------------------
# Exercise 2: Append new string in the middle of a given string
# s1 = "Ault"
# s2 = "Kelly"
# mid = round(len(s1)/2)
# s1_characters = [x for x in s1]
# s1_characters.insert(mid,s2)
# new_string = "".join(s1_characters)
# print(new_string)
# ---------------------------------------------------
# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# s1 = "America"
# s2 = "Japan"

# print(s1[0],s2[0],s1[int(len(s1)/2)],s2[int(len(s2)/2)],s1[-1],s2[-1],sep="")
# ---------------------------------------------------
# Exercise 4: Arrange string characters such that lowercase letters should come first
# str1 = "PyNaTive"
# list1=[]
# list2=[]
# for i in str1:
#     if i.islower():
#         list1.append(i)
#     else:
#         list2.append(i)
# print("".join(list1+list2))     
# ---------------------------------------------------
# Exercise 5: Count all letters, digits, and special symbols from a given string
# str1 = "P@#yn26at^&i5ve"
# letter , digit , special_symbol = 0,0,0
# for i in str1:
#     if i.isalpha():
#         letter += 1
#     elif i.isdigit():
#         digit += 1
#     else:
#         special_symbol += 1
# print(f'''Total counts of chars, digits, and symbols 
# Chars = {letter}
# Digits = {digit} 
# Symbol = {special_symbol}''')
# ---------------------------------------------------
# Exercise 6: Create a mixed String using the following rules
# s1 = "Abc"
# s2 = "Xyz"
# s3 = s1[0] + s2[-1] +s1[1] +s2[1] +s1[-1] + s2[0] 
# print(s3)
# ---------------------------------------------------
# Exercise 7: String characters balance Test
# s1 = "Ynf"
# s2 = "PYnative"
# sum_ = 0
# for char in s1:
#     if char in s2:
#         sum_+=1
# if sum_ == len(s1):
#     print(True)
# else:
#     print(False)


# ---------------------------------------------------
# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case "USA"
# str1 = "Welcome to USA. usa awesome, isn't it?"
# x = str1.replace(".","")
# sum_=0
# for i in x.split():
#     if i.lower() == "usa":
#         sum_+=1
# print(sum_)
# ---------------------------------------------------
# Exercise 9: Calculate the sum and average of the digits present in a string
# str1 = "PYnative29@#8496"
# nums = list(map(int,filter(lambda x: x.isdigit(),str1)))

# print(f"Sum = {sum(nums)} \nAverage = {sum(nums)/len(nums)}")
# ---------------------------------------------------
# Exercise 10: Write a program to count occurrences of all characters within a string
# str1 = "Apple"
# dict_count = {}
# for i in str1:
#     dict_count[i] = str1.count(i)

# print(dict_count)
# ---------------------------------------------------
# Exercise 12: Find the last position of a given substring
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# for i in str1.split():
#     if i == "Emma":
#         print(str1.rfind(i))
# ---------------------------------------------------
# Exercise 13: Split a string on hyphens
# str1 = "Emma-is-a-data-scientist"
# print(str1.split("-"))
# ---------------------------------------------------
# Exercise 14: Remove empty strings from a list of strings
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# str_list = list(filter( lambda x: x!="",str_list))
# print(str_list)
# ---------------------------------------------------
# Exercise 15: Remove special symbols / punctuation from a string
# import string
# str1 = "/*Jon is @developer & musician"
# # str1 = list(filter(lambda x:x.i))
# new_str = str1.translate(str.maketrans("","",string.punctuation))
# print(new_str)
# ---------------------------------------------------
# Exercise 16: Removal all characters from a string except integers
# str1 = 'I am 25 years and 10 months old'
# new_str = list(filter(lambda x:x.isdigit(),str1))
# print("".join(new_str))

# ----------------------------------------------------
# Exercise 17: Find words with both alphabets and numbers
# str1 = "Emma25 is Data scientist50 and AI Expert"
# str2 = str1.split(" ")
# for word in str2:
#     has_alpha = False
#     has_numeric = False
    
#     for char in word:
#         if char.isalpha():
#             has_alpha = True
#         elif char.isdigit():
#             has_numeric = True
    
#     if has_alpha and has_numeric:
#         print(word)

# for word in str2:
#     if any(char.isalpha() for char in word) and any(char.isdigit() for char in word):
#         print(word)
# -------------------------------------------------
# Exercise 18: Replace each special symbol with # in the following 
# import string

# str1 = '/*Jon is @developer & musician!!'
# new_str = str1.translate(str.maketrans(string.punctuation, '#' * len(string.punctuation)))
# print(new_str)
