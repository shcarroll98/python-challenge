import os
import csv
import pandas as pd
import pathlib as Path
#import election data set and make it a dataframe
csv_path = ("C:/Users/secar/OneDrive/Documents/Bootcamp/New folder/Starter_Code/PyPoll/Resources/election_data.csv")

election_df = pd.read_csv(csv_path, encoding="UTF-8")
#check the first 5 rows
election_df.head()

#sum up the amount of votes, making sure there are no repeats
#referenced substack for the nunique() function
uniqueballotid = election_df['Ballot ID'].nunique()
print("Total Votes:", uniqueballotid)

#grabbing each unique name from the Candidate row
#referenced substack for the unique function
candidates = election_df['Candidate'].unique()
for name in candidates:
    print(name)

Charles = 'Charles Casper Stockham'
charlescount = (election_df['Candidate'] == Charles).sum()
charlespercent = (charlescount / uniqueballotid)*100
formatcharles = "{:.3f}".format(charlespercent)
Diana = 'Diana DeGette'
dianacount = (election_df['Candidate'] == Diana).sum()
dianapercent = (dianacount / uniqueballotid)*100
formatdiana = "{:.3f}".format(dianapercent)
Raymon = 'Raymon Anthony Doane'
raymoncount = (election_df['Candidate'] == Raymon).sum()
raymonpercent = (raymoncount / uniqueballotid)*100
formatraymon = "{:.3f}".format(raymonpercent)
print("Charles Casper Stockham:", formatcharles, charlescount)
print("Diana DeGette:", formatdiana, dianacount)
print("Raymon Anthony Doane:", formatraymon, raymoncount)

#create a dictionary using the names and percentages calculated above
results = {'Charles Casper Stockham': 23.049, 'Diana Degette': 73.817, 'Raymon Anthony Doane': 3.139} 
#find the maximum within the dictionary
winner = max(results, key=results.get)
#print the winner
print(f"Winner: {winner}")
