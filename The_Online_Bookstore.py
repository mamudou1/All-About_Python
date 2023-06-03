def calculate_total_cost(order_total, is_international):
    if order_total >= 50 and is_international =="N" :
        shipping_fee = 0
    elif order_total >= 0  and is_international =="Y":
        shipping_fee = 10
    else:
        shipping_fee = 5
    
    total_cost = order_total + shipping_fee
    return total_cost


# Prompt the user for order total
order_total = float(input("Enter the order total: "))

# Prompt the user for international status
is_international = input("Is the order international? (Y/N): ").upper() == "Y"

# Calculate the total cost
total_cost = calculate_total_cost(order_total, is_international)

# Display the total cost of the order
print("Total cost of the order: $", total_cost)
