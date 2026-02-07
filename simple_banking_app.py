def check_balance(account):
    pass

def deposit(account, amount):
    pass

def withdraw(account, amount):
    pass


balances = 0

while True:
    print("Welcome to Simple Banking App")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        print(f"Your balance is: ${balances}")
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        balances += amount
        print(f"${amount} deposited. New balance is: ${balances}")
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balances:
            print("Insufficient funds!")
        else:
            balances -= amount
            print(f"${amount} withdrawn. New balance is: ${balances}")
    elif choice == '4':
        print("Thank you for using Simple Banking App. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")