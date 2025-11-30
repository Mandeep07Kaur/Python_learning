customer_name = "Mandeep"
is_member = True
fruits = ["apple", "banana", "kiwi"]

print("Customer name is: " ,customer_name)
print("Membership Status: ", is_member)
print(fruits)
print(len(fruits))
fruits.append("grapes")
is_member = (not(is_member))
print(fruits)
print(is_member)