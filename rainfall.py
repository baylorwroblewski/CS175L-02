# CS175
#Baylor Wroblewski
# rainfall.py

total_rainfall = 0
monthly_rainfall = 0
average_rainfall = 0
num_years = int(input("Enter the number of years (1, 2, or 3)? "))
while num_years != 1 and num_years != 2 and num_years != 3:
    print("Invalid number of years, please enter again.")
    num_years = int(input("Enter the number of years (1, 2, or 3)? "))
    

for x in range(1, num_years+1):
    print("For year", x, ":")
    for x in range(12):
        rainfall = float(input("Enter the amount of rainfall for the month: "))
        total_rainfall = total_rainfall + rainfall

total_months = num_years * 12
print(f"For {total_months} months")
print(f"Total rainfall: {total_rainfall:.2f} inches")

average_rainfall = total_rainfall/total_months
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
