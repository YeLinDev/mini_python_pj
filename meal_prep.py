child = float(input("What is the price of a child's meal? : "))
adult = float(input("What is the price of an adult's meal? : "))
ice_cream = float(input("What is the price of a ice-cream? : "))
children = int(input("How many children are there? : "))
adults = int(input("How many adults are there? : "))
ice_creams = int(input("How many ice-cream do you want? : "))
tax = float(input("What is the sales tax rate? : "))

print()
subtotal= (child*children)+(adult*adults)+(ice_cream*ice_creams)
print(f"Subtotal: {subtotal}")
sale_tax= (subtotal*tax)/100
print(f"Sales Tax: {sale_tax}")
total= subtotal+sale_tax
print(f"Total: {total}")
print()

cus_pay= float(input("What is the payment amount? : "))
change= cus_pay-total
print(f"Change: {change:.2f}")