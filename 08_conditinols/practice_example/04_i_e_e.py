'''
WAP to print electricity bill (accept number of unit from user), according to following criteria.

First 100 units = no charge
Next 100 units = rs 5 per unit
After 200 units = rs 10 per unit
'''

bill = int(input("Enter the units: "))

if(bill <= 100):
    print("No charge..!")
elif(bill > 100 and bill <= 200):
    rs = (bill - 100)*5
    print("Total amount payable:", rs)
elif(bill > 200):
    rs1 = 500 + (bill  - 200) * 10
    print("Total Amount payable: ", rs1)
else:
    print("Invalid number or units")