def deposit(balance, amount):
    balance = balance + amount
    return balance

def withdraw(balance, amount):
    if balance < amount:
        print("Insufficient funds")
        return balance
    else:
        return balance - amount
    
balance = 500

balance = deposit(balance, 200)
print("Balance after deposit:", balance)
balance = withdraw(balance, 100)
print("Balance after deposit:", balance)
balance = withdraw(balance, 800)
print("Balance after deposit:", balance)


