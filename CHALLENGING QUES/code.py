accounts = []
acc_no = 1001
transaction_history = {}

def create_account(name, balance):
    global acc_no
    acc_details = {
        "Acc_no": acc_no,
        "Name": name,
        "Balance": balance
    }
    accounts.append(acc_details)
    transaction_history[acc_no] = []
    transaction_list = transaction_history[acc_no]
    transaction_list.append(f"{name}'s account  has been created with initial balance {balance} and account number {acc_no}")
    print(f"{name}'s account  has been created with account number {acc_no}\n")
    acc_no += 1

def deposit(acc_no, deposit):
    for dict in  accounts:
        if dict["Acc_no"] == acc_no:
            dict["Balance"] += deposit
            break
    else:
        print("No account found with this account number")
    transaction_list = transaction_history[acc_no]
    transaction_list.append(f"₹{deposit} has been deposited")
    print(f"₹{deposit} has been deposited\n")

def withdraw(acc_no, withdraw):
    for dict in accounts:
        if dict["Acc_no"] == acc_no:
            if dict["Balance"] > withdraw:
                dict["Balance"] -= withdraw
                break
            else:
                print("Not enough balance to withdraw")
                break
    else:
        print("No account found with this account number")
    transaction_list = transaction_history[acc_no]
    transaction_list.append(f"₹{withdraw} has been withdrawn")
    print(f"₹{withdraw} has been withdrawn\n")

def transfer(sender_ano, receiver_ano, transfer):
    for dict in accounts:
        if dict["Acc_no"] == sender_ano:
            if dict["Balance"] > transfer:
                dict["Balance"] -= transfer
                break
            else:
                print("Not enough balance to transfer")
                break
    else:
        print("No account found with this account number")

    for dict in accounts:
        if dict["Acc_no"] == receiver_ano:
            dict["Balance"] += transfer
            break
    else:
        print("No account found with this account number")
    transaction_list1 = transaction_history[receiver_ano]
    transaction_list1.append(f"₹{transfer} has been transferred into this account")
    transaction_list2 = transaction_history[sender_ano]
    transaction_list2.append(f"₹{transfer} has been transferred from this account")
    print(f"₹{transfer} has been transferred from {sender_ano} account to {receiver_ano} account\n")

print("Razod's Bank \n")
print("Let us create ur account first")

name = input("Enter your name: ")
initial_balance = int(input("Your initial balance: "))
create_account(name, initial_balance)

print("\nNow what do you want to do with your account ?")

ans = "y"

while ans == "y":

    print("1: Create a new account")
    print("2: Deposit balance")
    print("3: Withdraw balance")
    print("4: Transfer balance")
    print("5: Get you transaction history")

    response = int(input("\nEnter your response: "))

    if response == 1:
        name = input("Enter your name: ")
        initial_balance = int(input("Your initial balance: "))
        create_account(name, initial_balance)
    elif response == 2:
        acno = int(input("Enter your account number: "))
        deposit_amount = int(input("Enter the amount that you want to deposit: "))
        deposit(acno, deposit_amount)
    elif response == 3:
        acno = int(input("Enter your account number: "))
        withdraw_amount = int(input("Enter the amount that you want to withdraw: "))
        withdraw(acno, withdraw_amount)
    elif response == 4:
        sender_acno = int(input("Enter sender's account number: "))
        receiver_acno = int(input("Enter receiver account number: "))
        transfer_amt = int(input("Enter the amount that you want to transfer: "))
        transfer(sender_acno, receiver_acno, transfer_amt)
    elif response == 5:
        acno = int(input("Enter the account number of which you want transaction history: "))
        for i in transaction_history[acno]:
            print(i, "\n")

    ans = input("Want another operation ? (y/n) ")

print("\nThankyou for using our service")