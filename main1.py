#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:03:05 2023

@author: joshuagibson
"""

import os
import csv

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
count1 = 0
count2 = 0
count3 = 0
percent1 = 0
percent2 = 0
percent3 = 0
value_counts = 0
winner = None

candidate_name = None

election = os.path.join('..', 'Resources', 'election_data.csv')

with open (election) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        total_votes += 1
        list1 = candidate
        
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


set_candidate = set(list1) 
list_candidate = (list(set_candidate))
 
candidate1 = list_candidate[0]
candidate2 = list_candidate[2]
candidate3 = list_candidate[1]

votes_percentage1 = (candidate_votes[candidate1] / total_votes) * 100
votes_percentage2 = (candidate_votes[candidate2] / total_votes) * 100
votes_percentage3 = (candidate_votes[candidate3] / total_votes) * 100 
          

x = max(candidate_votes[candidate1], candidate_votes[candidate2], candidate_votes[candidate3])       


if x == candidate_votes[candidate1]:
    winner = candidate1
elif x == candidate_votes[candidate2]:
    winner = candidate2
else:
    winner = candidate3



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