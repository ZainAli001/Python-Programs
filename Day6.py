# Exercise 1: Reverse a list in Python
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)
# -----------------------------------------------------------
# Exercise 2: Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# res = [i+j for i,j in zip(list1,list2)]
# print(res)
# -----------------------------------------------------------
# Exercise 3: Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = list(map(lambda x: x**2,numbers))
# print(res)
# -----------------------------------------------------------
# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# res = [x+y for x in list1 for y in list2]
# print(res)
# -----------------------------------------------------------
# Exercise 5: Iterate both lists simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for i , j in zip(list1,list2[::-1]):
#     print(i,j)
# -----------------------------------------------------------
# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# res = list(filter(None, list1))
# print(res)
# -----------------------------------------------------------
# Exercise 7: Add new item to list after a specified item

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7) 
# print(list1)
# -----------------------------------------------------------
# Exercise 8: Extend nested list by adding the sublist 
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# # sub list to add
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)
# -----------------------------------------------------------
# Exercise 9: Replace list’s item with new value if found
# list1 = [5, 10, 15, 20, 25, 50, 20]
# pos = list1.index(20)
# list1[pos] = 200
# print(list1)

# -----------------------------------------------------------
# Exercise 10: Remove all occurrences of a specific item from a list.
# list1 = [5, 20, 15, 20, 25, 50, 20]
# res = list(filter( lambda x: x!= 20,list1))
# print(res)
