#compilation of lists basics

#A list is a data type that contains multiple values in an ordered state

fruits = ["apple", "banana", "mango","orange"]

#indexing starts at position zero in a list

colors = ["red", "blue", "yellow", "green"]
print(colors.index('red'))
print(colors.index('blue'))
print(colors.index('yellow'))
print(colors.index('green'))

#printing out message using individual list values

fruits = ["apple", "banana", "mango","orange"]

print(f"{fruits[0]} have a red and green variety")
print(f"{fruits[1]} havent grown much this year")
print(f"{fruits[2]} is really popular in the market")

#Modifying and Manipulating Lists
#changing, adding and removing
numbers = [1, 2, 3, 4, 5]

numbers[1] = 5 #changing elements in a list
print(numbers)

numbers.append(7) #adding numbers to a list
print(numbers)

numbers.remove(1) #removing elements from a list
print(numbers)

numbers.pop(4)      #removing an element from a list and using it somewhere else
new_number = numbers.pop()

count = numbers.count(1)  #shows the number of occurence of a specific element in a list
print(count)

numbers.insert(4, 7)  #insert an element at a specified index
print(numbers)

numbers_1 = [6, 7, 8, 9]
numbers.extend(numbers_1)   #adds a list to another list
print(numbers)

print(min(numbers)) #finds the smallest value
print(max(numbers)) #finds the largest value

#Sorting a Lists
random_numbers = [12, 18, 84, 56, 74, 23, 125, 56, 785]
random_numbers.sort() #sorts the list peramanently
print(random_numbers)

new = sorted(random_numbers, reverse = True) #using sorted method
print(new)

last_item = random_numbers[-1] #access the last item on the list
print(random_numbers)

#LOOPING THROUGH A LIST
languages = ['python', 'java', 'ruby', 'c++']

print("These are examples of progamming languages: ")
for language in languages:
    print(f"{language}")
    

#square every number in a list
nums = [2, 3, 4, 5]
squares = []
print(nums)
print("The squares of these numbers are: ")

for i in nums:
    square = i**2
    squares.append(square)
    
print(squares)

#another loop example
items = ['books', 'pens', 'pencils', 'bags']
print("necessities: ")
for i in items:
    print(f" -{i}")

print("all items printed")

#Working with part of a list
favourite_food = ['meat', 'fruits', 'rice', 'fries', 'chicken']

new = favourite_food[:3] #slicing through a list
new = favourite_food[3:5]

#looping thru a slice
favourite_food = ['meat', 'fruits', 'rice', 'fries', 'chicken']

for i in favourite_food[:3]:
    print(i)
    
#copy a list using slicing
numbers = [6, 7, 8, 9]

new_numbers = numbers[:]
print(numbers)
print(new_numbers)


#defining a tuple
cities = ('nairobi', 'mombasa', 'kisumu', 'nakuru')

for i in cities:
    print(i)
    
#overwriting a tuple
nums = (1,2,3,4)
nums = (4,5,6,7)

#shopping list program

shopping_list = []

products = input("Enter items: ").split()
for i in products:
    shopping_list.append(i)
    
print("Items to be bought:")
for item in shopping_list:
    print(f" -{item}")
    
item_to_delete = input("Enter item to remove: ")
if item_to_delete in shopping_list:
    shopping_list.remove(item_to_delete)
    print(f"    -{item_to_delete} has been removed from the list")
else:
    print(f"{item_to_delete} does not exist")

print(f"Updated shopping list: ")
for i in shopping_list:
    print(f"-{i}")