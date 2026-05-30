# Simple Bill Splitter
# (Used in apps like Splitwise)

print("\n\t==BILL SPLITTER==\n")

#get the total bill amount from the user
total_bill=float(input("Enter the total bill amount: ₹"))

#get the number of people to split the bill
num_people=int(input("Enter the no. of people splitting: "))

#split the bill using formula total_amount_of_bill/no. of ppls ( use the condition no. of ppls > 0 )
print("\n\t==RESULT==\n")
print(f"Total bill amount: ₹{total_bill}")
print(f"No. of people to split the bill: {num_people}")

#logic is main 
if num_people < 0:
    print("❌ Invalid! Number of people cannot be negative.")
elif num_people == 0:
    print("😂 You're paying the whole bill! 👾")
else:
    amount_per_person = total_bill / num_people
    print(f"Each Person Pays  : ₹{amount_per_person:.2f}")

