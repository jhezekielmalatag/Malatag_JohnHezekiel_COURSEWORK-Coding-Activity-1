# Shopping Cart
cart = {'apple': 2, 'banana': 5, 'milk': 2}

print("Current Cart:")
items = list(cart.items())
for i in range(len(items)):
    if i == len(items) - 1:
        print("and " + items[i][0] + f" ({items[i][1]} items)")
    else:
        print(items[i][0] + f" ({items[i][1]} items), ", end="")
print("\n")

# Add items to the cart
item = input("Enter the item you want to add: ").lower()
quantity = int(input("Enter the quantity: "))

#Check if the item is already in the cart
if item in cart:
    cart[item] += quantity
else:
    cart[item] = quantity
    
# Print the updated cart
print("Updated Cart:")
items = list(cart.items())
for count, item in enumerate(items):
    if count == len(items) - 1:
        print(f"and {count} {item}{'s' if count > 1 else ''}.")
    else:
        print(f"{count} {item}{'s' if count > 1 else ''}, ", end="")