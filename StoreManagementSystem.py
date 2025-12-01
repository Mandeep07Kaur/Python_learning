inventory = [
    {"name":"Milk", "qty":10},
    {"name":"Rice", "qty":20},
    {"name":"Water", "qty":40}
     ]

def add_product(inventory, name,qty ):
    product = {"name": name, "qty": qty}
    inventory.append(product)
    return inventory

def is_low_stock(product):
    if product["qty"] < 10:
        return True
    else:
        return False


cart = []

def add_to_cart(cart, product_name):
    cart.append(product_name)
    return cart

cart = add_to_cart(cart, "Milk")
cart = add_to_cart(cart, "Rice")


print(inventory)
print(is_low_stock(inventory[2]))
print(cart)

balance = 1000

def deposit(balance, amount):
    balance = balance + amount
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print ("Insufficient funds")
        return balance
    else:
        return balance - amount
    
employees = [
    {"name": "Riya", "present" : True},
    {"name": "Priya", "present" : False},
    {"name": "Anaya", "present" : True}
]

def count_present(employees):
    count = 0
    for emp in employees:
        if emp["present"] == True: 
         count += 1
    return count

balance = deposit(balance, 700)
print("Balance after deposit: " , balance)

balance = withdraw(balance, 400)
print("Balance after withdraw: " , balance)

balance = withdraw(balance, 100)
print("Balance after withdraw: " , balance)

print(count_present(employees))
