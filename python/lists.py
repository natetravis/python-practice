#printing numbers from 0 to a million
numbers = range(0, 1000001)

for number in numbers:
    print(number)

#printing out the maxmimum and minimum numbers in the range
print(max(numbers))
print(min(numbers))

#how fast can python add a million numbers
result = sum(range(1, 1000001))
print(result)

#printing odd numbers from 1 to 20
odd = list(range(1, 20, 2))

for odd_numbers in odd:
    print(odd_numbers)
    

#A list of multiples of three
multiples_of_3 = []
 
for number in range(3, 31):
    if number % 3 ==0:
        multiples_of_3.append(number)
        
for multiple in multiples_of_3:
    print(multiple)
 
    
#A list of the first 10 cubes
cubes = []

for value in range(1, 10):
    cube = value**3
    cubes.append(cube)
print(cubes)


#Cube Comprehension of the first ten cubes
cubes = [value**3 for value in range(1, 10)]
print(cubes)


#copying a list
my_food = ['pizza,', 'falafel', 'carrot cake', 'chicken', 'meat']
friend_food = my_food[:]

print("My favourite foods are " + my_food)
print("\nMy freind's favourite foods are: " + friend_food)

#copying select items using slice
print(my_food[1:4])

#using for loop to print the list
print("my favourite food: ")
for pizza in friend_food:
    print(pizza)

print("\nFriend's favourite food: ")    
for food in my_food:
    print(food)


