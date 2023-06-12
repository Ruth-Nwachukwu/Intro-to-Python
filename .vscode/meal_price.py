child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult meal? "))
children_num = int(input("How many children are there? " ))
adult_num = int(input("How many adult are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))
print()

subtotal = float(child_meal * children_num) + (adult_meal * adult_num)
salestax = float(sales_tax_rate / 100) * (subtotal)
total = float(salestax + subtotal)

print(f"Subtotal: ${subtotal}")
print(f"Sales Tax: ${salestax}")
print(f"Total: ${total}")

tip = float(input("Satisfied? Please leave a tip: $"))

print()
payment = float(input("What is the payment amount? "))
change = (payment) - (total) -(tip)

#formating change to 2 decimal places
print(f"Change: ${change:.2f}")