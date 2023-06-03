def calculate_total_cost(order_total, is_international):
    if order_total >= 50:
        shipping_fee = 0
    elif is_international:
        shipping_fee = 10
    else:
        shipping_fee = 5
    
    total_cost = order_total + shipping_fee
    return total_cost


while True:
    try:
        # Prompt the user for order total
        order_total = float(input("Enter the order total: "))
        if order_total <= 0:
            raise ValueError("Order total should be a positive number.")

        # Prompt the user for international status
        order_status = input("Is the order international? (Y/N): ").upper()
        if order_status not in ['Y', 'N']:
            raise ValueError("Invalid order status. Please enter 'Y' or 'N'.")

        is_international = order_status == "Y"

        # Calculate the total cost
        total_cost = calculate_total_cost(order_total, is_international)

        # Display the total cost of the order
        print("Total cost of the order: $", total_cost)

        break

    except ValueError as error:
        print("Error:", error)
