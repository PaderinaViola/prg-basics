###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Check pin")
    print("6. Change pin")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        
    elif choice == '5':
        check = input("Enter your password for checking: ")
        if len(check) == 4 and check.isdigit():
            print(f"Your password is ok!")
        else:
            print(f"Yor password is bad :( ")
        break  # Exit the loop
    elif choice == '6':
        change = input("Enter your new password: ")
        if len(change) == 4 and change.isdigit():
            print(f"Successfully сhanged your password!")
        else:
            print(f"Your password doesnt fit some criteria")
    else:
        print("Invalid option. Please try again.")
