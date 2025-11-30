def add_item(cart, item):
    cart.append(item)
    return cart

    
cart = ["milk", "bread"]

cart = add_item(cart, "butter")
cart = add_item(cart, "eggs")

print(cart)

def get_total_items(cart):
   return len(cart)

print(get_total_items(cart))