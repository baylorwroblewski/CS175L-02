#Expense Pie Chart
#Baylor Wroblewski
#CS 175L
import matplotlib.pyplot as plt

def main():
    # initialize variables
    categories = []
    amounts = []

    # open file and read data
    try:
        with open('expenses.txt', 'r') as file:
            for line in file:
                line = line.strip()
                #checks to make sure the line is not empty
                #then assigns each value to the their catagory
                if len(line) > 0: 
                    label, cost = line.split('\t')
                    #sends the values to seperate lists
                    try:
                        amount = int(cost)
                        categories.append(label)
                        amounts.append(amount)
                    except ValueError:
                        print(f"Error: {cost} is not a valid integer.")

        # create pie chart
        plt.pie(amounts, labels = categories, colors =('r','m','c','g','y','b'), autopct='%.2f%%')
        plt.title('Monthly Expenses')
        plt.show()

    except IOError:
        print("Error: Could not open file 'expenses.txt'.")

if __name__ == '__main__':
    main()
