def add_product(inventory, product_name, quantity):
    product = {"name": product_name, "qty": quantity}
    inventory.append(product)
    return inventory

inventory = []

inventory = add_product(inventory, "Milk", 10)
inventory = add_product(inventory, "Bread", 5)
inventory = add_product(inventory, "Eggs", 30)

def is_low_stock(product):
    if product["qty"] < 10:
        return True
    else:
        return False
    

print(inventory)    
print(is_low_stock(inventory[2]))


