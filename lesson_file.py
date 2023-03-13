1 task
a=10
b=20
if a==b:
    print ("equal")
else:
    print ("not equal")

2 task
name = input("please enter your name ")
age = int(input("please enter your age "))
if age == 18:
    print("you are welcome")
elif age >= 18:
    print ("you are welcome")
else:
    print("next time,baby")
    
 3 task
for a in range (0, 100):
    if a % 7 == 0:
        print(a)
 4 task
word = input("please write a word, you want to reverse ")
reverse = word [::-1]
print(reverse)

5 task ( current date - deltatime)
from datetime import date, timedelta
dt = date.today() - timedelta(4)
print('Current Date :',date.today())
print('4 days before Current date is:',dt)

6 task reverse a string
def my_function(x):
    return x[::-1]

mytxt = my_function("1234abcd")

print(mytxt)
7 task find the max of three numbers

def maximum(a, b, c):

    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


# Driven code
a = 10
b = 14
c = 12
print(maximum(a, b,c)
      
task for homework :
      import os
import datetime

# Create the input screen
name = input("Enter your name: ")
surname = input("Enter your surname: ")
id_num = input("Enter your ID number: ")

# Create the directory name based on today's date
today = datetime.date.today().strftime("%Y-%m-%d")
directory_name = os.path.join(os.getcwd(), today)

# Create the directory if it doesn't exist
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

# Create the file name based on the ID number
file_name = os.path.join(directory_name, f"{id_num}.txt")

# Write the user's information to the file
with open(file_name, "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Surname: {surname}\n")
    f.write(f"ID number: {id_num}\n")

# Output all saved information on the screen
for filename in os.listdir(directory_name):
    with open(os.path.join(directory_name, filename), "r") as f:
        print(f.read())
