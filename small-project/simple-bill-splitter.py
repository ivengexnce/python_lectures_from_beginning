# Simple Bill Splitter
# (Used in apps like Splitwise)

print("\n\t==BILL SPLITTER==\n")

#get the total bill amount from the user
total_bill=float(input("Enter the total bill amount: "))

#get the number of people to split the bill
num_people=int(input("Enter the no. of people to  split the bill in: "))

#split the bill using formula total_amount_of_bill/no. of ppls ( use the condition no. of ppls > 0 )

if num_people >0:
    amount_per_person_pays=total_bill/num_people
    print("Each person gets the contri of: ", amount_per_person_pays)

else:
    print("You have to pay all bill😂👾")


