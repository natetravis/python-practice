#using for loop on tuples
fruits = ('apple', 'banana', 'mango', 'pineapple', 'grapes')

print("Fruits availabe: ")
for fruit in fruits:
    print(fruit)

fruits[0] = 'dates' #Returns TypeError: 'tuple' object does not support item assignment. Immutable data structure


#Reassinging the variables values changes the value in a tuple
fruits = ('apples', 'dates', 'watermelon', 'pineapple', 'grapes')
print("\nUpdated Fruits: ")

for fruit in fruits:
    print(fruit)