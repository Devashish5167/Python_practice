import sys
accBalance = 10000

print("....Hello! Welcome To ATM....")
print("Please choose your option: \n 1.Check Balance \n 2.WithDraw \n 3.Deposit Cash \n 4.Deposit Check")
option = int(input("Choose one of the Option: "))
# sys.argv


if option == 1:
    print(f"Your total account balance is {accBalance}")
elif option == 2:
    withdraw = int(input("Enter withdraw amount: "))
    if withdraw > accBalance:
        print("Insufficient Withdraw Amount Entered")
    else:
        print("Your Entered Amount is Withdrawing ....")
        print(f"Your Total Amount : {accBalance-withdraw}")
elif option == 3:
    Dcash = int(input("Entered Deposit Cash Amount: "))
    print(f"Total Amount after deposit Cash: {accBalance + Dcash}")
elif option == 4:
    Dcheque = int(input('Enter the deposit Check amount: '))
    print(f"Total Amount after deposit Cash: {accBalance + Dcheque}")
    
