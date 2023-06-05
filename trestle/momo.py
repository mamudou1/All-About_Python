def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_net_cash_flow():
    print("==== Net Cash Flow Calculation ====")
    transactions_received = get_valid_input("Enter the total number of mobile money transactions received: ")
    transactions_sent = get_valid_input("Enter the total number of mobile money transactions sent: ")
    amount_received = get_valid_input("Enter the total amount received through mobile money transactions: ")
    amount_sent = get_valid_input("Enter the total amount sent through mobile money transactions: ")

    net_cash_flow = amount_received - amount_sent
    print("Net cash flow for the day: ", net_cash_flow)


calculate_net_cash_flow()
