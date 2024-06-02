print("Welcome to our Bank ABC")

password = 1234
choice = 0
balance = 50000
pin = int(input("Enter your pin: "))

if pin == password:
    while True:
        print("Enter your choice")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = int(input())

        if choice == 1:
            print("Your Balance is", balance)

        elif choice == 2:
            withdraw = int(input("Enter amount you want to withdraw: "))
            if withdraw <= balance:
                balance -= withdraw
                print("Your withdraw amount is", withdraw)
                print("Remaining balance is", balance)
            else:
                print("Insufficient Amount")

        elif choice == 3:
            deposit = int(input("Enter amount you want to deposit: "))
            balance += deposit
            print("Your deposited amount is", deposit)
            print("Your balance amount is", balance)

        elif choice == 4:
            print("Exit")
            break

        else:
            print("Invalid choice. Please try again!")
else:
    print("Your Pin is Incorrect. Please Try again!")
