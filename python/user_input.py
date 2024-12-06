#Simple program requesting for a user input
prompt = input("What kind of rental car do you like? ")

print("let me see if I can find you a Subaru")

#Restuarant Seating
prompt = int(input("How many people are in your dinner group? "))

if prompt > 8:
    print(f"They'll have to wait for a table")
else:
    print(f"Their table is ready")
    
#multiples of ten
prompt = int(input("Enter number: "))

if prompt % 10 == 0:
    print(f"It is a multiple of ten")
else:
    print(f"It is not a multiple of ten")
    
#pizza toppings
prompt = "Enter pizza toppings: "
prompt += "\n Enter quit to end program"

message = " "
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

#pizza toppings example 2
prompt = "Enter pizza toppings: "
prompt += "\nEnter 'quit' to end the program: "

while True:
    message = input(prompt)
    if message.lower() == 'quit':
        break
    elif message.strip():
        print(f"Added {message} to your pizza!")
    else:
        print("Please enter a valid topping!")
    
    
#Movie tickets
while True:
    age_input = input("Enter age (or type 'quit' to exit): ")
    
    if age_input.lower() == 'quit':
        print("Thank you! Have a great day!")
        break
    
    if age_input.isdigit():
        age = int(age_input)
        
        if age < 3:
            print("Ticket is free\n")
        elif age <= 12:
            print("Ticket is $10\n")
        else:
            print("Ticket is $15\n")
    else:
        print("Invalid input. Please enter a valid age or 'quit'.")

# Pizza Toppings - Conditional Test in While Loop
prompt = "Enter a pizza topping (or 'quit' to exit): "

topping = input(prompt)
while topping != 'quit':  # The loop stops when the user enters 'quit'
    print(f"Adding {topping} to your pizza!")
    topping = input(prompt)

print("Thank you! Your pizza is ready!")

# Movie Tickets - Active Variable to Control Loop
prompt = "Enter your age (or 'quit' to finish): "

active = True  # Active variable to control the loop
while active:
    age_input = input(prompt)
    
    if age_input.lower() == 'quit':  # Stop the loop when the user enters 'quit'
        active = False
        print("Goodbye!")
    elif age_input.isdigit():  # Validate the input is a number
        age = int(age_input)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
    else:
        print("Invalid input. Please enter a valid age or 'quit'.")

# Pizza Toppings - Break Statement
prompt = "Enter a pizza topping (or 'quit' to exit): "

while True:  # Infinite loop controlled by a break statement
    topping = input(prompt)
    if topping.lower() == 'quit':  # Break out of the loop when 'quit' is entered
        print("Thank you! Your pizza is ready!")
        break
    print(f"Adding {topping} to your pizza!")


# List of sandwiches
sandwiches_orders = [
    "Club Sandwich",
    "BLT Sandwich",
    "Grilled Cheese Sandwich",
    "Ham and Cheese Sandwich",
    "Caprese Sandwich",
    "Turkey Cranberry Sandwich",
    "pastarami",
    "pastarami",
    "pastarami",
]

finished_sandwiches = []
message = "deli has ran out of pastarami"
while 'pastarami' in sandwiches_orders:
    sandwiches_orders.remove('pastarami')
print(sandwiches_orders)

while sandwiches_orders:
    available_sandwiches =sandwiches_orders.pop()
    print(f"\nI made you a {available_sandwiches}")
    finished_sandwiches.append(available_sandwiches)

print("\nThe following sandwiches have been made: ")
for sandwich in finished_sandwiches:
    print(sandwich)

# Empty list to store responses
vacation_responses = []

# Poll prompt
print("Welcome to the Dream Vacation Poll!")
print("If you could visit one place in the world, where would you go?")

# Start a loop to collect responses
while True:
    # Ask user for their response
    response = input("Enter your dream vacation destination (or 'quit' to end): ")
    
    # Break the loop if the user types 'quit'
    if response.lower() == 'quit':
        break
    
    # Add the response to the list
    vacation_responses.append(response)

# Print the results of the poll
print("\nDream Vacation Poll Results:")
for i, response in enumerate(vacation_responses, 1):
    print(f"{i}. {response}")
