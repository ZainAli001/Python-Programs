# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# res = []
# odd_element = l1[1::2]
# even_element = l2[0::2]
# res.extend(even_element)
# res.extend(odd_element)
# print(res)

# ---------------------------------------------------
# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
# list1 = [54, 44, 27, 79, 91, 41]
# print(f"Orignal List = {list1}")
# x= list1.pop(4)
# print(f"List after remove the item at index 4 = {list1}")
# list1.insert(2,x)
# print("List after add the item at index 2",list1)

# ---------------------------------------------------
# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# len_list = len(sample_list)
# chunk_size = int(len_list/3)
# start = 0
# end =chunk_size
# for i in range(3):
#     list_chunk = sample_list[start:end]
#     print(f"Before Reverse {list_chunk}")
#     print(f"After Reverse {list(reversed(list_chunk))}")
#     start = end
#     end+=chunk_size
# ---------------------------------------------------
# Exercise 4: Count the occurrence of each element from a list
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# number_dict = {}
# for i in sample_list:
#     number_dict[i] = sample_list.count(i)
# print(number_dict)
# ---------------------------------------------------
# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
# first_list =  [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]

# res = set(zip(first_list,second_list))
# print(res)
# ---------------------------------------------------
# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}

# res = first_set.intersection(second_set)
# for item in res:
#     first_set.remove(item)
# print(first_set)
# ---------------------------------------------------
# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set

# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}
# print("First set is subset of second set -",first_set.issubset(second_set))
# print("Second set is subset of second set -",second_set.issubset(first_set))
# print()
# print("First set is Super set of second set -",first_set.issuperset(second_set))
# print("Second set is Super set of second set -",second_set.issuperset(first_set))

# first_set.clear()
# print(first_set)
# print(second_set)

# -----------------------------------------------------
# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

# for num in roll_number:
#     if num in sample_dict.values():
#         print(f"{num} is present in the dictionary")
#     else:
#         roll_number.remove(num)

# print(roll_number)  
 
# -----------------------------------------------------
# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# list1 = []
# for val in speed.values():
#     if val not in list1:
#         list1.append(val)

# print(list1)
# -----------------------------------------------------
# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number

# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

# print(f"Original List = {sample_list}")

# filter_list = tuple(filter(lambda x: sample_list.count(x) ==1, sample_list))
# print(filter_list)
# print(max(filter_list))
# print(min(filter_list))