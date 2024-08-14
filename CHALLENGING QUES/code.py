accounts = []
acc_no = 1001

def create_account(name, balance):
    global acc_no
    acc_details = {
        "Acc_no": acc_no,
        "Name": name,
        "Balance": balance
    }
    accounts.append(acc_details)
    acc_no += 1

def deposit(acc_no, deposit):
    for dict in  accounts:
        if dict["Acc_no"] == acc_no:
            dict["Balance"] += deposit
            break
    else:
        print("No account found with this account number")

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


create_account("alsamad", 15000)
create_account("ansh", 5000)
deposit(1002, 20000)
withdraw(1002, 5000)
transfer(1002, 1001, 10000)
print(accounts)