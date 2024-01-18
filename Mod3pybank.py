import os
import csv
import pandas as pd
import pathlib as Path

#import CSV as dataframe
csv_path = ("C:/Users/secar/OneDrive/Documents/Bootcamp/New folder/Starter_Code/PyBank/Resources/budget_data.csv")
budget_df = pd.read_csv(csv_path, encoding="UTF-8")
#inspect dataframe
budget_df.head()

#checking amount of rows in the dataset
budget_df.info()

#dropping any duplicate months
uniquerows = budget_df.drop_duplicates(subset='Date').shape[0]
#getting the sum of the Profit/Loss amounts
totalprofit = budget_df['Profit/Losses'].sum()
print("Total Months:", uniquerows)
print("Total:", totalprofit)

#to avoid comparing a tuple with an integer
for i, profit_value in enumerate(budget_df['Profit/Losses']):
  #skip the first row since there's no previous row to compare  
    if i > 0:
        #setting up the formula for checking the profit difference
        profitdifference = profit_value - budget_df.loc[i - 1, 'Profit/Losses']
        #checking that profit difference is working
        print(f"Profit difference at index {i}: {profitdifference}")

#creating a list to store the differences
profit_differences = []

for i, profit_value in enumerate(budget_df['Profit/Losses']):
    # Skip the first row since there's no previous row to compare
    if i > 0:
        profit_difference = profit_value - budget_df.loc[i - 1, 'Profit/Losses']
#append the profit differences to the empty list
        profit_differences.append(profit_difference)

# Calculate the average of profit differences
average = sum(profit_differences) / len(profit_differences)
#2 decimal places in the result, taken from stack overflow
formattedaverage = "{:.2f}".format(average)
#print Average
print("Average:", formattedaverage)

#initializing with the first element of profit_differences
maxamount = profit_differences[0]
#for loop for grabbing the maximum amount in the ist
for amount in profit_differences:
    if amount > maxamount:
        maxamount = amount
print(f"Greatest Increase in Profits:", maxamount)

#initalize greatest decrease

minamount = profit_differences[0]

for m in profit_differences:
    if m < minamount:
        minamount = m
#print greatest decrease
print("Greatest Decrease in Profits:", minamount)




