team = 'arsenal'
print("Is team == 'arsenal'? I predict True")
print(team == 'arsenal')

print("\nIs team == 'arsenal'? I predict False")
print(team == 'man u')

car = 'benz'
print("Is car == 'Benz'? I predict True")
print(car == 'benz')

print("\nIs team == 'benz'? I predict False")
print(car == 'bmw')

print("\nIs car.lower() == 'benz'? I predict True")
print(car.lower() == 'benz')

print("\nIs car != 'audi'? I predict True")
print(car != 'audi')

print("\nIs len(car) == 4? I predict True")
print(len(car) == 4) 

print("\nDoes car.startswith('b')? I predict True")
print(car.startswith('b'))

print("\nIs car == 'bmw'? I predict False")
print(car == 'bmw')

print("\nIs car == 'Benz'? I predict False")
print(car == 'Benz')#case sensitive

print("\nIs car.endswith('z') and car == 'audi'? I predict False")
print(car.endswith('z') and car == 'audi')

print("\nIs len(car) > 5? I predict False")
print(len(car) > 5)

#numeric comparison
print(5 > 3) 
print(2 == 10) 

#string comparison
print("apple" == "apple")  
print("banana" < "apple") #alphabetic comparison

#list length
print(len([1, 2, 3]) == len([4, 5, 6])) 
print(len([1, 2]) > len([1, 2, 3]))  

#membership
print("a" in "apple") 
print("z" in "apple") 

#boolean logic
print(True and False)
print(True or False) 


