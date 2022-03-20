item_list = []
price_list = []

print("Welcome to Snack and Soda Machine Cart")
print()

while True:

    print("Please select one of the following:")
    print()
    print("1. Add item \n2. View cart\n3. Remove item\n4. Compute total\n5. Quit")
    print()
    choice = int(input("Please enter an action:  "))
    print()
    if choice == 1:
        item = input("What item would you like to add? ")
        price = input(f"What is the price of {item}? ")
        item_list.append(item)
        price_list.append(price)
        print(f"{item} was added to the list")
        print()
    elif choice == 2:
        print(f"The contents of the shopping cart are:")
        for i in range(len(item_list)):
            item = item_list[i]
            price = price_list[i]
            print(f"{i}. {item} - ${price} ")
        print()
    elif choice == 3:
        remove = int(input("Which item would you like to remove? "))
        cart.pop(item)
        item_list.pop(remove)
        price_list.pop(remove)
    elif choice == 4:
        print(f"The total is: ${sum(item_list)}") # empty for now
        print()
    elif choice == 5:
        print(f"Thank you. Goodbye.")
    else:
        print("This is not a valid input, please try again")
        break
