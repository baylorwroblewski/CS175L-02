#Baylor Wroblewski
#CS175-02
#stocks

amountP = 40.00
commissionPP = 0.03
amountS = 42.75
commissionPS = 0.03
numberS = 2000.00

amountP = numberS*amountP
commissionP = amountP*commissionPP
amountS = numberS*amountS
commissionPS = amountS*commissionPS
profitS = amountP + commissionP + commissionPS
profit = amountS - profitS

print("Amount paid for the stock: ${:,.2f}".format(amountP))
print("Commission paid on the purchase: ${:,.2f}".format(commissionP))
print("Amount the stock sold for: ${:,.2f}".format(amountS))
print("Commission paid on the sale: ${:,.2f}".format(commissionPS))
print("Profit (or loss if negative): ${:,.2f}".format(profit))

