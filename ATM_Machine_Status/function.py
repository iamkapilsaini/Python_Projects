# import main
# import record
'''
import json

def deposite():
    try:
        amount = int(input("Enter the amount that you want to deposite : "))
        # with open("record.py", "w" ) as f:
        #     f.write(amount)

        if amount <= 0:
            print("Enter a positive amount.")
            return

        balance = getbalance()  # Read previous balance
        balance = balance + amount  # Update balance
        (balance)  # Save updated balance

        print("Current balance:", balance)

    except (FileNotFoundError, json.JSONDecodeError):
        return 0



def withdraw():
    pass

def getbalance():
    try:
        with open("record.json", "r") as f:
                return json.load(f)["balance"]

    except (FileNotFoundError, json.JSONDecodeError):
        return 0    
        # print(f"\nYour Current Balance is{balance[-1]} Rs")

'''


from record import load_record, save_record

def getbalance():
    data = load_record()
    return data["balance"]


def deposite():
    amount = int(input("Enter deposit amount: "))

    if amount <= 0:
        print("Enter a positive amount.")
        return

    data = load_record()

    data["balance"] += amount
    data["deposite"].append(amount)

    save_record(data)

    print("Deposit successful!")
    print("Current balance:", data["balance"])


def withdraw():
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a positive amount.")
        return

    data = load_record()

    if amount > data["balance"]:
        print("Insufficient balance!")
        return

    data["balance"] -= amount
    data["withdraw"].append(amount)

    save_record(data)

    print("Withdrawal successful!")
    print("Current balance:", data["balance"])
