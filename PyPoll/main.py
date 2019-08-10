
# coding: utf-8

# In[ ]:


import os
import csv

# Path to collect data
csv_path = os.path.join('Resources', 'election_data.csv')


# In[ ]:


get_ipython().system('head -n 2 Resources/election_data.csv')


# In[ ]:


def voter_stats(voter_data):
    ids.append(voter_data[0])
    county.append(voter_data[1])
    candidates.append(voter_data[2])
    total_votes = len(ids)
    khan = voter_data[2].count("Khan")
    correy = voter_data[2].count("Correy")
    li = voter_data[2].count("Li")
    otooley = voter_data[2].count("O'Tooley")
    percentK = (khan/total_votes)*100
    percentC = (correy/total_votes)*100
    percentL = (li/total_votes)*100
    percentO = (otooley/total_votes)*100
    return total_votes, khan, correy, li, otooley, percentK, percentC, percentL, percentO


# In[ ]:


# Read in the CSV file
ids = []
county = []
candidates = []
with open(csv_path, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for voter_data in csvreader:
        voter_stats(voter_data)

