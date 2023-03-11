import csv
import numpy as np
import pandas as pd
import string
from openpyxl import load_workbook

tickets = pd.read_excel("Ticket Data.xlsx", engine='openpyxl')
tickets = tickets.drop(columns=['SVD Assigned'])

#Standardizing Affected Name Column
def name_fix(name):
    fixed_name = ""
    if '(' in name: 
        fixed_name = name[:name.find('(')]
    else:
        fixed_name = name
    return fixed_name.strip()
tickets['Affected Name'] = tickets['Affected Name'].apply(name_fix)

with pd.ExcelWriter('Ticket Data.xlsx', mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    tickets.to_excel(writer, sheet_name='Tickets Cleaned')

#How many tickets were submitted by each user
user_count = tickets.groupby('Affected Name').Reference.count().reset_index()
user_count.columns = ['Affected User', 'Total Count']
#print(user_count)

#How many tickets did each employee have assigned to them
assigned_to = tickets.groupby('Assigned User Name').Reference.count().reset_index()
assigned_to.columns = ['Assigned User', 'Total Count']
#print(assigned_to)