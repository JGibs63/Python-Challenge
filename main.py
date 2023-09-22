#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:00:29 2023

@author: joshuagibson
"""
'import dependencies'
import os
import csv
'define and set variables'
date = []
net = []
difference = []
total_value = 0
total_months = 0
change_months = 0
total_change = 0
average_change = 0
profit_start = 0
profit_end = 0
max_increase = 0
max_decrease = 0
value = 0
current_row = 0
difference = 0
DifferenceRow = []


'set path to data resource'
main = os.path.join('..', 'Resources', 'budget_data.csv')

MonthRow = None
'open and read csv file, skip header row, append variables to each column. Count number of rows for total number of months'
with open (main) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        date.append(row[0])
        net.append(row[1])
        total_months += 1
        total_value += int(row[1])
        'find the difference between each row in order to find greatest increase and greatest decrease' 
        if MonthRow is not None:
            current_row = int(MonthRow[1])
            next_row = int(row[1])
            difference = next_row - current_row
            DifferenceRow.append(difference)
            if difference > max_increase:
                max_increase = difference
                increase_date = row[0]
            elif difference < max_decrease:
                max_decrease = difference
                decrease_date = row[0]
                
        MonthRow = row    
        'finding the average change'     
    if net:
         profit_start = int(net[0])
         profit_end = int(net[-1])
         change_months = total_months - 1
         total_change = profit_end - profit_start
         average_change = total_change / change_months
            
        
    'print results'    
        
print("Financial Analysis")
print("------------------------------------------")
print("Total months: ", total_months)
print("Total: $", end='')
print(total_value)
print("Average change: $", end='')
print (round(average_change, 2))
print(f"Greatest Increase In Profits: {increase_date} (${max_increase})")
print(f"Greatest Decrease In Profits: {decrease_date} (${max_decrease})")
        