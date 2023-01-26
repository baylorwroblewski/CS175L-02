#Baylor Wroblewski
#CS175-02
#stocks

#receives input from user
amountP = float(input("Please enter the amount paid per stock: "))
amountS = float(input("Please enter the amount each stock sold for: "))
commission = float(input("Please enter the commission rate: "))
numberS = float(input("Please enter the number of stock bought: "))

#calculations
amountP = numberS*amountP
commissionP = amountP*commission
amountS = numberS*amountS
commissionPS = amountS*commission
profitS = amountP + commissionP + commissionPS
profit = amountS - profitS

#prints out calculations
print(" ")
print("Amount paid for the stock: ${:,.2f}".format(amountP))
print("Commission paid on the purchase: ${:,.2f}".format(commissionP))
print("Amount the stock sold for: ${:,.2f}".format(amountS))
print("Commission paid on the sale: ${:,.2f}".format(commissionPS))
print("Profit (or loss if negative): ${:,.2f}".format(profit))

