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
    
    
#Looping through usernames
usernames = ["admin", "user1", "user2", "user3", "user4"]

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report")
    else:
        print("Hello" + username + " thank you for logging in,")

#no users in the list
usernames = ["admin", "user1", "user2", "user3", "user4"]

usernames.clear()

if not usernames:
    print("We need to find some users")
    
    
#Checking 
current_users = ["admin", "Eric", "Sophia", "James", "Liam"]

new_users = ["Sophia", "Olivia", "Emma", "Noah", "Eric"]

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Sorry the username {new_user} is already taken" )
    else:
        print(f"The username {new_user} is available")
    