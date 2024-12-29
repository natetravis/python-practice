balance = 0  # Initialize the global balance variable
is_running = True  # Variable to keep the program running

def show_balance():
    global balance  # Use the global balance variable
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("Not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdrawn: "))
    global balance  # Use the global balance variable
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero")
        return 0
    else:
        return amount

def main():
    global balance  # Use the global balance variable
    global is_running  # Use the global is_running variable

    while is_running:
        print("\nBanking Program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance()
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw()
        elif choice == '4':
            is_running = False
        else:
            print("Not a valid choice")
    print("Thank you for using the banking program!")

if __name__ == '__main__':
    main()
