#If statement

#simple conditional program
number = int(input("Enter number: "))

if number > 0:
    print("positive")
else:
    print("not positive")

#conditional statements
while True:
    age = int(input("Enter age: "))

    if age  >= 18:
        print(True)
    elif 13 <= age <= 18:
        print("teen")
    elif 5 <= age <= 12:
        print("kid")
    else:
        print("toddler")
        break

#checking for inequality
message = input("enter a string: ")

if message == "string":
    print(True)
else:
    print(False)
    
#ignoring case when checking for inequality
while True:
    
    enter = input("Enter string: ")
    enter = enter.lower()

    if enter == "String".lower():
        print(True) 
    else:
        print(False)
        break

#checking multiple conditions
number = 25

if number >= 10 and number <= 50:
    print("Between range")
else:
    print("not in range")

colors = ['red', 'blue', 'yellow', 'green', 'black']

if 'red' in colors:
    print(True)
    
if 'white' not in colors:
    print(True)
    
numbers = [1, 2, 3, 4, 5, 6]

if 5 in numbers:
    print("found it!")


#if-elif-else chain
grade = int(input("Enter score: "))

if 90 <= grade < 94:
    print("A")
elif grade > 95:
    print("Distinction")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
else:
    print("FAIL")