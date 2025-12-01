accounts = [
    {"name": "Mandeep", "balance": 500, "transactions": [] },
    {"name": "deep", "balance": 1500, "transactions": [] },
    {"name": "ririra", "balance": 5500, "transactions": [] }

]

def add_account(accounts, name, balance):
    new_account = {"name": name, "balance": balance, "transactions": []}
    accounts.append(new_account)
    return accounts

def deposit(accounts, name, amount):
    for account in accounts:
        if account["name"] == name:
            account["balance"] += amount
            account["transactions"].append(f"Deposited {amount}")
            print("Deposited", amount)
            return accounts
    print("Account not found")
    return None

def withdraw(accounts, name, amount):
    for account in accounts:
        if account["name"] == name:
            if account["balance"] >= amount:
                 account["balance"] -= amount
                 account["transactions"].append(f"Withdrew {amount}")
                 return accounts
            else:
                print ("Insufficient funds")
                return None
    print("Account not found")
    return None

def get_balance(accounts, name):
    for account in accounts:
        if account["name"] == name:
            return account["balance"]
    print("Account not found")
    return None

def get_transactions(accounts, name):
    for account in accounts:
        if account["name"] == name:
            return account["transactions"]
    
    print("Account not found")
    return None
   

def search_account(accounts, name):
    for account in accounts:
        if account["name"] == name:
            return account
        
    print("Account not found")
    return None
