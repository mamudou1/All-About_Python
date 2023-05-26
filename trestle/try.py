def calculate_notes(denominations, amount):
    # Initializing variables to count the number of each note
    num_1_notes = 0
    num_2_notes = 0
    num_5_notes = 0

    # Calculating the number of each note based on the available denominations
    while amount >= denominations[2]:  # Check if 5 notes can be used
        num_5_notes += 1
        amount -= denominations[2]

    while amount >= denominations[1]:  # Check if 2 notes can be used
        num_2_notes += 1
        amount -= denominations[1]

    while amount >= denominations[0]:  # Check if 1 notes can be used
        num_1_notes += 1
        amount -= denominations[0]

    return num_1_notes, num_2_notes, num_5_notes

# Input denominations
denominations = [1, 2, 5, 10, 20, 50]

# Taking input from the user
amount = int(input("Enter the amount: "))

# Calculating the number of notes
num_1_notes, num_2_notes, num_5_notes = calculate_notes(denominations, amount)

# Displaying the result
print("Number of 1 notes:", num_1_notes)
print("Number of 2 notes:", num_2_notes)
print("Number of 5 notes:", num_5_notes)