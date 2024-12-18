#simple dictionary
books ={"title": 'splinter cell', "author": 'tom clancy', "year": 2009}
print(books)

#updating a dictionary
books["genre"] = 'action'
print(books)

#accessing values in a dictionary
print(books["author"])

#starting with an empty dictionary
country = {}

country["country"] = 'kenya'
country["capital"] = 'nairobi'
country["population"] = "50 million"

print(country)

#modifying values in a dictionary
country["capital"] = 'nakuru'
print(country)

#removing key value pairs
del country["country"]
print(country)


#Advanced dictionary operations
fruits = {"apples": 3, "banana": 5, "cherry": 4, "mangoes": 6}

print("Dictionary of Fruits: ")
for fruit, quantity in fruits.items():
    print(f"{fruit}: {quantity}")

#loop to display all keys
for fruit in fruits.keys():
    print(f"Keys: {fruit}")
    
#using sorted to loop through the dict:
for fruit in sorted(fruits.keys()):
    print(f"Keys: {fruit}")

#loop through all values
for quantity in fruits.values():
    print(f"values: {quantity}")
    
#nesting a list of dictionaries
cars = [
    {"brand": 'toyota', "model": 'corolla'}
    {"brand": 'Honda', "model": 'civic'}
    {"brand": 'Ford', "model": 'mustang'}
    {"brand": 'tesla', "model": 'model S'}
]

for car in cars:
    print(f"Brand: {car['brand'].title()}, Model: {car['model'].title()}")
    
#a list in a dictionary
student = {"student": ['bio', 'physics', 'chem', 'comp sci', 'math']}

print("these are the subjects for this sem: ")
for subject in student["student"]:
    print(f'\t {subject}')

#a dictionary in a dictionary
city = {
    "name": 'nairobi',
    "details": {
        "weather": {
            "temprature": "15 deg", 
            "condition": 'cloudy'
        },
        "population": {
            "count": 52656464,
            "denisty": "5655 people per km2"
        }
    }
}

print(f"city: {city['name']}")
print(f"weather: {city['details']['weather']['condition']}")