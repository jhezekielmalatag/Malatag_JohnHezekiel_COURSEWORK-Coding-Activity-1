# Create friends list:
friends = ["Jimboy", "Vhony", "Angel", "Hezekiel"]

# Display the list in one line
print("Current friends list:")
for i in range(len(friends)):
    if i == len(friends) - 1:
        print("and " + friends[i])
    else:
        print(friends[i] + ", ", end="")
print("\n")

# Ask the user what they want to do
choice = input("Do you want to add or remove a name? (add/remove): ").lower()

if choice == "add":
    name = input("Enter the name to add: ")
    friends.append(name)
    print(f"{name} has been added.")

elif choice == "remove":
    name = input("Enter the name to remove: ")
    if name in friends:
        friends.remove(name)
        print(f"{name} has been removed.")
    else:
        print("That name is not in the list.")

else:
    print("Invalid choice.")

# Sort the list alphabetically
friends.sort()

# Print the updated, sorted list
print("Updated friends list:")
for i in range(len(friends)):
    if i == len(friends) - 1:
        print("and " + friends[i])
    else:
        print(friends[i] + ", ", end="")
        
loop = input("Do you want to loop through the list? (yes/no): ").lower()