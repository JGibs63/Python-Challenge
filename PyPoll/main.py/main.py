#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:03:05 2023

@author: joshuagibson
"""
'import dependencies'
import os
import csv

'define and set variables'
voter_id = []
county = []
candidate = []
candidate_name1 = None
candidate_name2 = None
candidate_name3 = None
candidate_count = 0
total_votes = 0
candidate_options = []
candidate_votes = {}
value_counts = 0
winner = None
candidate_name = None

'csv file path to data resource'
election = os.path.join('..', 'Resources', 'election_data.csv')

'open and read csv, skip header, append each column, and count total rows for total votes'
with open (election) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        total_votes += 1 
        'define list for later formatting'
        list1 = candidate
        'append candidate names in order to count votes with candidate_votes function'       
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

'converted cndidate list for preferred formatting purposes'
set_candidate = set(list1) 
list_candidate = (list(set_candidate))
 
candidate1 = list_candidate[0]
candidate2 = list_candidate[2]
candidate3 = list_candidate[1]
'find votes percentage by dividing candidate votes by total votes'
votes_percentage1 = (candidate_votes[candidate1] / total_votes) * 100
votes_percentage2 = (candidate_votes[candidate2] / total_votes) * 100
votes_percentage3 = (candidate_votes[candidate3] / total_votes) * 100 
          
'find max value in order to determine winner'
x = max(candidate_votes[candidate1], candidate_votes[candidate2], candidate_votes[candidate3])       
if x == candidate_votes[candidate1]:
    winner = candidate1
elif x == candidate_votes[candidate2]:
    winner = candidate2
else:
    winner = candidate3

'print results'

print("Election Results")
print("---------------------------------------")
print("Total votes: ", total_votes)
print("---------------------------------------")
print(f"{candidate1}: {round(votes_percentage1, 3)}% ({candidate_votes[candidate1]})") 
print(f"{candidate2}: {round(votes_percentage2, 3)}% ({candidate_votes[candidate2]})") 
print(f"{candidate3}: {round(votes_percentage3, 3)}% ({candidate_votes[candidate3]})")
print("---------------------------------------")
print("Winner: ", winner)
print("---------------------------------------")

PyPoll_txt = os.path.join("PyPoll_output.txt")
with open(PyPoll_txt, "w") as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("----------------------------------------\n")
    txtfile.write(f"Total votes: {total_votes}\n")
    txtfile.write("---------------------------------------\n")
    txtfile.write(f"{candidate1}: {round(votes_percentage1, 3)}% ({candidate_votes[candidate1]})\n")
    txtfile.write(f"{candidate2}: {round(votes_percentage2, 3)}% ({candidate_votes[candidate2]})\n")
    txtfile.write(f"{candidate3}: {round(votes_percentage3, 3)}% ({candidate_votes[candidate3]})\n")
    txtfile.write("---------------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("---------------------------------------\n")
    