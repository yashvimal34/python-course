'''
WAP  to accept the cost price of bike and display the road tax of a bike according to following criteria:
> 100000   15%
> 50000  and < = 100000   10%
< = 50000  5%
'''
tax = 0
pr = int(input("Enter the bike cost price: "))

if(pr > 100000):
    tax = 15/100*pr
    print("Total amount of bike is:", tax)
elif(pr > 50000 and pr <= 100000):
    tax = 10/100*pr
    print("Total amount of bike is ", tax)
elif(pr <= 50000):
    tax = 5/100*pr
    print("Total amount if bike is: ", tax)
else:
    print("no charge")