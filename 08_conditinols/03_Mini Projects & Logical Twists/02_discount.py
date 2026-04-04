dis = (int(input("Enter the Purchase amount: ")))

purchase = 0

if (dis >= 5000 ):
    purchase = dis*0.20
    print("Congratualations Sir, You got a discout of 20 percent on puchasing products above Rs: 5000. ")
elif (dis >= 3000):
    purchase = dis*0.10
    print("Congratualations Sir, You got a discout of 10percenr on puchasing products above Rs: Rs. 3000 to 4999. ")
elif (dis < 3000):
    purchase = dis
    print("Sorry Sir, No Discount.")
else:
    ("You cannot purchase anything")

    # Calculate final amount
final_amount = dis - purchase

# Print result
print(f"Discount Applied: ₹{purchase:.2f}")
print(f"Final Amount to Pay: ₹{final_amount:.2f}")
