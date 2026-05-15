# Taking total amount as input from user
Amount = int(input("Please enter amount for Withdraw :"))

# Calculating the number of notes of different denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10


print("Notes of 100 rupee is", note_1)
print("Notes of 50 rupee is", note_2)
print("Notes of 10 rupee is", note_3)