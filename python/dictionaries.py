#printing information from a dictionary

info = {'first_name': 'doe', 'last_name': 'john', 'city': 'nairobi'}

print(info) #prints the entire dictionary
print(info['city'])#prints out a single value
print(info['first_name'])
print(info['last_name'])

#print out each person's data
favourite_numbers = {'saka': 7, 'kai': 29, 'martin': 8, 'timber': 12, 'saliba': 2}

for name, number in favourite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")
    
#model a dictionary from a dictionary
definitions = {
    "tuples": "Immutable sequences in Python used to store collections of items.",
    "loops": "Structures that allow repetitive execution of a block of code until a specified condition is met.",
    "lists": "Mutable sequences in Python that store collections of items and allow modifications.",
    "dictionary": "A collection of key-value pairs in Python, where each key is unique and used to access its corresponding value.",
    "if statement": "A conditional structure used to execute a block of code if a specified condition evaluates to True.", "variables": "Containers for storing data values that can be changed during program execution.",
    "functions": "Reusable blocks of code that perform a specific task and can accept input and return output.",
    "strings": "Sequences of characters used to store text in Python, enclosed in single or double quotes.",
    "comments": "Lines in the code that are ignored during execution, used for documentation. Indicated by a `#` symbol.",
    "integers": "Whole numbers (positive or negative) without a fractional part, used for numerical operations."
}

for word, meaning in definitions.items():
    print(f"\n{word.title()}: {meaning}")
    
#more looping examples with dictionaries
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'mississipi': 'usa'}

for river, country in rivers:
    print(f"\nThe {river.title()} runs through {country.title()}")
    
#print each river
for river in rivers.values():
    print(f"River: {river.title()}")
    
#print each country
for country in rivers.values():
    if country.lower() == 'usa':
        print(country.upper())
    else:
        print(country.title())


# Dictionary of people and their favorite languages
favorite_languages = {
    "alice": "python",
    "bob": "java",
    "charlie": "c++",
    "diana": "ruby"
}

people_to_poll = ["alice", "bob", "ethan", "frank", "diana"]

for person in people_to_poll:
    if person.lower() in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, please take our favorite languages poll!")

#list with dictionaries
info = {'first_name': 'doe', 'last_name': 'john', 'city': 'nairobi'}
info_1 = {'first_name': 'top', 'last_name': 'dawg', 'city': 'nakuru'}
info_2 = {'first_name': 'big', 'last_name': 'biggie', 'city': 'mombasa'}

people = [info, info_1, info_2]

for names in people:
    print(f"\nDetails about the person: ")
    for key, value in names.items():
        print(f"{key.title()}: {value.title()}")
        
        
#pets
bella = {"kind": "dog", "owner": "Alice"}
whiskers = {"kind": "cat", "owner": "Bob"}
tweety = {"kind": "bird", "owner": "Charlie"}
nemo = {"kind": "fish", "owner": "Diana"}
buster = {"kind": "hamster", "owner": "Ethan"}

pets = [bella, whiskers, tweety, nemo, buster]

for pet in pets:
    print(f"\nDetails about the pet:")
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")
        
#favourite places
favorite_places = {
    "alice": ["Paris", "New York", "Tokyo"],
    "bob": ["London", "Sydney"],
    "charlie": ["Rome", "Barcelona", "Dubai"]
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favourite places are:")
    for place in places:
        print(f"- {place}")
        
#dictionary in a dictionary
cities = {
    "Paris": {
        "country": "France",
        "population": 2148327,
        "fact": "Known for the Eiffel Tower and its rich history in art and culture."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 13929286,
        "fact": "The world's most populous metropolitan area."
    },
    "New York": {
        "country": "USA",
        "population": 8419600,
        "fact": "Famous for its iconic landmarks such as the Statue of Liberty and Times Square."
    }
}

for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
    