#Analyze voting results
#Step 1: Import dependencies
import os
import csv

#Next import the data
votedata = os.path.join('..','election_data.csv')

#Set up global variables
total_votes = 0
can_list = []
can1 = 0
can2 = 0
can3 = 0
can4 = 0

with open(votedata, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #set candidate name as a variable
        candidate_name = row[2]
        #Increase vote total
        total_votes += 1
        #Add new candidate to the list
        if candidate_name not in can_list:
            can_list.append(candidate_name)
        #Increase number by candidate name
        if candidate_name == can_list[0]:
            can1 += 1
        elif candidate_name == can_list[1]:
            can2 += 1
        elif candidate_name == can_list[2]:
            can3 += 1
        elif candidate_name == can_list[3]:
            can4 += 1
#calculate the resulting percentages of the vote
per1 = round((can1/total_votes)*100)
per2 = round((can2/total_votes)*100)
per3 = round((can3/total_votes)*100)
per4 = round((can4/total_votes)*100)

#determine the winner

#compare the first two candidates
if can1 > can2:
    forerunner1 = can1
    forerunner1_name = can_list[0]
else:
    forerunner1 = can2
    forerunner1_name = can_list[1]
#compare the last two candidates
if can3 > can4:
    forerunner2 = can3
    forerunner2_name = can_list[3]
else:
    forerunner2 = can4
    forerunner2_name = can_list[4]
#compare the forerunners
if forerunner1 > forerunner2:
    winner = forerunner1
    winner_name = forerunner1_name
else:
    winner = forerunner2
    winner_name = forerunner2_name
#create the reporting information and format it
report = (f"""Voting Report
*****************************
Total number of votes cast:{total_votes}
The candidates voted for were:{can_list}
{can_list[0]}:{can1} votes or {per1}%
{can_list[1]}:{can2} votes or {per2}%
{can_list[2]}:{can3} votes or {per3}%
{can_list[3]}:{can4} votes or {per4}%
The winner of the election is {winner_name} with {winner} votes.
""")
#show the report on screen
print(report)
#make a file to print the report as a text file
file = open("Vote_Report.txt","w")
file.write(report)
file.close()