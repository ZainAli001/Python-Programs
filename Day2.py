# Exercise 1: Accept numbers from a user
a,b = input("Enter number = ").split()
print(int(a)*int(b))

# ---------------------------------------------
# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
print("Name","Is","James",sep="**")
# ---------------------------------------------
# Exercise 3: Convert Decimal number to octal using print() output formatting
num = 8
print('%o' % num)
print(f'{num:o}')
#  ---------------------------------------------
# Exercise 4: Display float number with 2 decimal places
num = 458.541315
print('%.2f' % num)
print(f"{num:.2f}")
# ---------------------------------------------
# Exercise 6: Write all content of a given file into a new file by skipping line number 5
with open("test.txt","r") as f:
    with open("new.txt","w") as g:
        for line in f:
            if int(line.strip()[-1]) != 5:
                g.write(line)
            
# ---------------------------------------------
# Exercise 8: Format variables using a string.format() method.
totalMoney = 1000
quantity = 3
price = 450
print("I have {0} dollars so I can buy {1} football for {2:.2f} dollars.".format(totalMoney,quantity,price))
# ---------------------------------------------
# Exercise 9: Check file is empty or not
import os 
size = os.stat("test.txt").st_size
if size == 0:
    print("file empty")
else:
    print("file No empty")

# # ---------------------------------------------
# Exercise 10: Read line number 4 from the following file
with open("test.txt","r") as f:
    for line in f:
        if int(line.strip()[-1]) == 4:
            print(line)
