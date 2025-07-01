account_number = 1234
pin_number = 6971
balance = 5000

while True:
    acount = int(input("Enter account number: "))
    pin = int(input("Enter a pin: "))
    
    if(acount == account_number and pin == pin_number):
        print("Login Succesful")
        break
    else :
        print("invlaid credential")

while True:
    print("\n-- ATM menu ---")
    print("1. Withdraw Money")
    print("2. Deposit Money")
    print("3. Check balance")
    print("4. Change Pin")
    print("5. Exit ")
    
    choice = int(input("Enter coice: "))
    
    if (choice==1):
        while True:
            amount = int(input("Enter amount you want to withdraw: "))
            if(amount <= balance ):
                balance -= amount
                print("Withdraw Succesful, New Balance: " ,balance)
                break
            else:
                print("Insufficent amount")
    
    if (choice == 2):
        amount = int(input("Enter amount: "))
        balance += amount
        print("Deposit Succesful, New balance: " ,balance)
    
    
    elif (choice == 3):
        balance = 5000
        print("Your balance is : " ,balance)
    
    elif (choice == 4):
        while True:
            old_pin = int(input("Enter old pin: "))
            if (old_pin == pin_number):
                new_pin = int(input("Enter new pin: "))
                new_pin = pin_number
                break
            else:
                print("Wrong pin")
    
    elif (choice == 5):
        print("Thank you, Existing..")
        break
    
    else:
        ("Invalid Choice. Please try again")

    