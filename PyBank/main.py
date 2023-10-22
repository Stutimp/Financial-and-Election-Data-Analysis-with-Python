# Importing csv and os libraries 
import csv
import os
# Set the path to the resource folder and  to the file
path_to_csv = os.path.join('Resources','budget_data.csv')

#Initializing some variables to keep track of our datapoints
months = 0
net = 0
profit_loss_list = []
months_list = []
greatest_increase = 0
greatest_decrease = 0

# Opening the CSV file using open() and reading through 'csv.reader'
with open(path_to_csv, 'r') as file:

    #Store all the text inside a vriable called "budget_file"
    budget_file = csv.reader(file)

    # print the contents of the file and printing the headers
    print(budget_file)

    header = next(budget_file)
   
    # Process the first row of data, initializing the 'net' and 'months' variables and storing the value of first month's profit /loss
    first_row =next(budget_file)
    net += int(first_row[1])
    months += 1
    next_month = int(first_row[1])

    #print(net)
    #print(months)

    # Looping through the remaining rows of the csv file to calculate various financial metrics
    for row in budget_file:
        profit_loss = int(row[1])  - next_month


        #calculating profit /loss difference compared to the previous month and append to the profit_loss_list
        profit_loss_list.append(profit_loss)

        #Appending month to months_list
        months_list.append(row[0])

        #Updating the 'net' and 'months' variable
        net += int(row[1])
        months += 1

        #updating with 'next_month variable for the next iteration
        next_month = int(row[1])

# Calculate the greatest increase and decrease in profit/loss
greatest_increase = max(profit_loss_list)
greatest_decrease = min(profit_loss_list)
    

        #print(profit_loss_list) 
       # print(months_list) 

  #Calculating and printing the greatest increase and decrease in profit/loss, along with the corresponding months.

                 
greatest_increase_month =months_list[profit_loss_list.index(greatest_increase)]
greatest_decrease_month = months_list[profit_loss_list.index(greatest_decrease)]

    #printing other financial metrics
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months:  {months}")
print(f"Total: $ {net}")
print(f"Average Change: $ {sum(profit_loss_list)/ len(profit_loss_list):.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
  





   





