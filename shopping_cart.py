print("Welcome to Snack and Soda Machine Cart")
print()

cart = []

while True:
    print("Please select one of the following:")
    print()
    print("1. Add item \n2. View cart\n3. Remove item\n4. Compute total\n5. Quit")
    print()
    choice = int(input("Please enter an action:  "))
    print()

    if choice == 1:
        item = input("What item would you like to add? ")
        cart.append(item)
        names = input(f"What is the price of {item}? ")
        cart.append(names)
        print(f"{item} was added to the list")
        print()
    elif choice == 2:
        print(f"The contents of the shopping cart are:")
        for i in cart:
            print(i)
        print()
    elif choice == 3:
        item = input("Which item would you like to remove? ")
        cart.pop(item)
        print(f"{item} was removed from the list")
        print()
    elif choice == 4:
        print(f"The total is:") # empty for now
        print()
    else:
        print(f"Thank you. Goodbye.")
        break
