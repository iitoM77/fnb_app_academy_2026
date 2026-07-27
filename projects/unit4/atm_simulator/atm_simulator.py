#fixed amount as the Balance
balance = 17000

#display the greeting message
print(f"Good day, your balance is: R{str(balance)}")

#prompt a message to ask the user to insert the amount they want to withdraw and cast it to int 
withdrawal = int(input("How much would you like to withdraw?: "))

#here I set the valid withdrawal rule i.e. the user can't withdraw more money than they have in the account and make sure they set an amount higher than R0
if withdrawal <= balance:
    new_balance = balance - withdrawal
    print(f"Withdrawal successful! Remaining balance: R{str(new_balance)}")
    receipt = input("would you like to display receipt? (y/n)")
    if receipt.lower() == "y":
        print(f"Here's your receipt")
        print(f"Balance: {str(balance)} - {str(withdrawal)} = {str(new_balance)}")
        print(f"Thank you and have a lovely day")
    else:
        print("Thank you and have a lovely day")
elif withdrawal <=0:
    print("Invalid amount. You must withdraw more than R0")
else:
    print("Declined. Insufficient funds")