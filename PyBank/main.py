
# coding: utf-8

# In[ ]:


import os
import csv

# Path to collect data
csv_path = os.path.join('Resources','budget_data.csv')


# In[ ]:


def financial_stats(bank_data):
    months.append(bank_data[0])
    money.append(bank_data[1])
    total_months = len(months)
    
    return
    


# In[ ]:


# Read in the CSV file
months = []
money = []
with open(csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(header)
    for bank_data in csvreader:
        financial_stats(bank_data)

