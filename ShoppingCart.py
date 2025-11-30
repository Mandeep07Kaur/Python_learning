cart = ["milk", "bread", "eggs"]
has_discount = False

print(cart)
print(len(cart))

cart.append("butter")

if len(cart) > 3:
    has_discount = True

print(cart)
print(has_discount)
