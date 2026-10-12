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
