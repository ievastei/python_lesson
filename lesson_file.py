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
print(maximum(a, b, c))
