#simple function definition
def greet_user():
    print("Hi there, functions innit")
greet_user()

#passing information to a function
def greet_user(name):
    print(f"a-yo {name} tryna learn python yeah?")
greet_user('bruv')

#arguments and parameters
def add_numbers(a, b):
    return a + b
total = add_numbers(5, 6)
print(total)

#working with arguments
def describe_city(city, country):
    print(f"The capital of {country} is {city}")

describe_city('kenya', 'nairobi')

def describe_city(city, country): #keyword argument
    print(f"The capital of {country} is {city}")

describe_city('nairobi', country= 'kenya')

#default values
def describe_city(city, country = 'USA'): #keyword argument
    print(f"The capital of {country} is {city}")

describe_city('DC')

#avoid argument errors
def divide_numbers(a, b):
    return a / b
total = divide_numbers(6) #only one argument given
print(total)

#Return Values
def square_number(n):
    return n**2
square = square_number(4)
print(square)

    #optional argument
def format_name(first_name, last_name = ''):
    if last_name:
        full_name = first_name + last_name
    else:
        full_name = first_name
    return full_name
name = format_name('top', 'dawg')
print(name)

name = format_name('bruv')
print(name)

    #retuning a dictionary
def build_profiles(first, last):
    person = {"firstname": first, "lastname": last}
    return person

name = build_profiles('top', 'dawg')
print(name)


#functions with loops and lists
def get_user_input():
    while True:
        message = input("Enter message or press q to quit: ")
        if message == 'q':
            break
    
get_user_input()


#passing a list
def print_fruits(fruits):
    for fruit in fruits:
        msg = f"-{fruit}"
        print(msg)
f = ['apples', 'mangoes', 'bananas']
print_fruits(f)

#modifying a list in a function
def process_order(orders, completed_orders):
    while orders: 
        current_order = orders.pop()
        print(f"Finalizing order: {current_order}")
        completed_orders.append(current_order)

    print("\nThe following orders have been completed:")
    for completed_order in completed_orders:
        print(f"- {completed_order}")

orders = ['iphone', 'samsung', 'huawei', 'pixel']
completed_orders = []

process_order(orders, completed_orders)

#prevent a function from modifiyng a list
def process_order(orders, completed_orders):
    pending_orders = orders[:]

    while pending_orders:  
        current_order = pending_orders.pop()
        print(f"Finalizing order: {current_order}")
        completed_orders.append(current_order)

    print("\nThe following orders have been completed:")
    for completed_order in completed_orders:
        print(f"- {completed_order}")


original_orders = ['iphone', 'samsung', 'huawei', 'pixel']
completed_orders = []

process_order(original_orders, completed_orders)

print("\nOriginal orders list remains unchanged:")
print(original_orders)
