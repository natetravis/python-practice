alien_color = ['green', 'yellow', 'red']

for color in alien_color:
    if color == 'green':
        print(str(5) + "points")
        
        
#fails the test     
alien_color = ['blue', 'yellow', 'red']

for color in alien_color:
    if color == 'green':
        print(str(5) + "points")
        

#if else chain
if alien_color == 'green':
    point = 5
else:
    point = 10

print("You just earned " + str(point) + " points")

#runs the else block
if alien_color == 'blue':
    point = 5
else:
    point = 10

print("You just earned " + str(point) + " points")

#if elif else chain
alien_color = ['blue', 'yellow', 'red']

if 'blue' in alien_color:
    point = 5
elif 'yellow' in alien_color:
    point = 10
elif 'red' in alien_color:
    point = 15
else:
    point = 0

print("You just earned " + str(point) + " points")


#checking a person's age
age = int(input("Enter age: ")) # Set the person's age

if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

    message = "elder"
    
print("This person is an" + message)
    

#checking if items exist on a list
fruits = ['apples', 'mango', 'pineapple', 'banana', 'watermelon', 'grapes']

if 'apples' in fruits:
    print("Yes we have apples")


#checking whether a value is not in a list
fruit = 'guavas'

if fruit not in fruits:
    print(fruit.title() + " is not in stock")