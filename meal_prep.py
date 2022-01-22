child = float(input("What is the price of a child's meal? : "))
adult = float(input("What is the price of an adult's meal? : "))
children = int(input("How many children are there? : "))
adults = int(input("How many adults are there? : "))
tax = float(input("What is the sales tax rate? : "))
print()
subtotal= (child*children)+(adult*adults)
print(f"Subtotal: {subtotal}")
sale_tax= (subtotal*tax)/100
print(f"Sales Tax: {sale_tax}")
total= subtotal+sale_tax
print(f"Total: {total}")
print()
cus_pay= float(input("What is the payment amount? : "))
change= cus_pay-total
print(f"Change: {change}")