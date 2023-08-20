# Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictonary = dict(zip(keys,values))
print(dictonary)
# -----------------------------------------------------------
# Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)
# -----------------------------------------------------------
# Exercise 3: Print the value of key ‘history’ from the below
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])
# -----------------------------------------------------------
# Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
dict1 = dict.fromkeys(employees,defaults)
print(dict1)
# -----------------------------------------------------------
# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
new_dict = {}
for i in sample_dict.items():
    if i in keys:
        new_dict[i] = sample_dict[i]

print(new_dict)
# ---------------------------------------------------------
# Exercise 6: Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
new_dic= {}
# Keys to remove
keys = ["name", "salary"]
for key in sample_dict.items():
    if key not in keys:
        new_dic[key] = sample_dict[key]
print(new_dic)

# second method

filter_dict ={key : value for key,value in sample_dict.items() if key not in keys}
print(filter_dict)  

# ----------------------------------------------------------
# Exercise 7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
        print(True)
# ----------------------------------------------------------
# Exercise 8: Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict.popitem()
sample_dict.update({"location":"New York"})
print(sample_dict)

# ----------------------------------------------------------
# Exercise 9: Get the key of a minimum value from the following dictionary

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

min_value = min(sample_dict.values())
for key,value in sample_dict.items():
    if value == min_value:
        print(key, value)
# ----------------------------------------------------------
# Exercise 10: Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] =8500
print(sample_dict)
