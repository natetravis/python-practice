favourtie_foods = []

def display_menu():
    print("\nOptions")
    print("1. Add Items")
    print("2. Remove Items")
    print("3. View Items")
    print("4. Sort Items")
    print("5. Exit Program")

def add():
    foods = input("Enter name: ").split()
    favourtie_foods.extend(foods)
    print("Food added to the list")

def remove_items():
    if favourtie_foods:
        item_to_delete = input("Enter item to delete: ")
        if item_to_delete in favourtie_foods:
            favourtie_foods.remove(item_to_delete)
            print(f"{item_to_delete} deleted")
        else:
            print(f"{item_to_delete} does not exist")
    else:
        print("List is empty")

def view():
    if favourtie_foods:
        print("Favourite Foods")
        print("\n".join(f" -{item}" for item in favourtie_foods ))
    else:
        print("The list is empty")

def sort_list():
    print("Sorted List: ")
    for i in sorted(favourtie_foods):
        print(f" -{i}")
        
while True:
    display_menu()
    choice = input("Enter choice (1-4)").strip()
    
    if choice == '1':
        add()
    elif choice == '2':
        remove_items()
    elif choice == '3':
        view()
    elif choice == '4':
        sort_list()
    elif choice == '5':
        print("Exiting the program. Bye")
        break
    else:
        print("Invalid choice, please enter a number between 1 and 4")