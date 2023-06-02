one_notes = 1
two_notes = 2
five_notes = 5
ten_notes = 10
twenty_notes = 20
fifty_notes = 50

# Taking input from the user
amount = int(input("Enter the amount: "))

# Calculating the number of each note based on the available denominations
num_1_cedis_notes = 0
num_2_cedis_notes = 0
num_5_cedis_notes = 0

if amount >= five_notes:  # Check if 5 notes can be used
    num_5_cedis_notes = amount //five_notes
    amount %= five_notes

if amount >= two_notes:  # Check if 2 notes can be used
    num_2_cedis_notes = amount // two_notes
    amount %= two_notes

if amount >= one_notes:  # Check if 1 notes can be used
    num_1_cedis_notes = amount // one_notes
    amount %= one_notes

# Displaying the result
print("Number of 1 cedis notes:", num_1_cedis_notes)
print("Number of 2 cedis notes:", num_2_cedis_notes)
print("Number of 5 cedis notes:", num_5_cedis_notes)
