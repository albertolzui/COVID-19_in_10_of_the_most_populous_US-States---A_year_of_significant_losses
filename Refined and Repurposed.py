#!/usr/bin/env python

# make sure to install these packages before running:
#pip install pandas
#pip install sodapy
import numpy as np
import pandas as pd
from sodapy import Socrata
import matplotlib.pyplot as plt
from title_cal import get_month
from title_cal import get_date
from population import get_population

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cdc.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cdc.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First <=50000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("9mfq-cb36", limit=50000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# Drop columns that are not required
result_1 = results_df.drop(columns=["consent_cases", "consent_deaths", "prob_cases", "pnew_case", "pnew_death",
                                    "prob_death", "conf_cases", "conf_death", "created_at", "new_case", "new_death",
                                    "tot_cases"])

# Selecting rows where the state is one of the 10 most populous in the US. 50 other states are hereby 'dropped'.
state_shed = result_1[result_1['state'].isin(['CA', 'FL', 'GA', 'IL', 'MI', 'NC', 'NY', 'OH', 'PA', 'TX'])]

# Update dataframe to show full state names rather than abbreviations
state_name = state_shed.replace(['CA', 'FL', 'GA', 'IL', 'MI', 'NC', 'NY', 'OH', 'PA', 'TX'],
                                ['California', 'Florida', 'Georgia', 'Illinois', 'Michigan', 'North Carolina',
                                 'New York', 'Ohio', 'Pennsylvania', 'Texas'])


# Selecting only rows where the submission date is the same as the given date
data = state_name[state_name['submission_date']=='2021-01-12T00:00:00.000']
data2 = state_name[state_name['submission_date']=='2022-01-12T00:00:00.000']

# Fetching the date from the dataframe as a string for subsequent use/ operations
date1 = get_date(data)
date2 = get_date(data2)

# Breaking up the date element to day, month and year
year1 = date1[0:4]
month1 = date1[5:7]
day1 = date1[8:]

year2 = date2[0:4]
month2 = date2[5:7]
day2 = date2[8:]

# Passing the month number into the get_month() function to return the month name.
actual_month1 = get_month(month1)
actual_month2 = get_month(month2)

# Getting the dataframe ready for plotting
df = pd.DataFrame(data, columns=["state", "tot_death"])
df2 = pd.DataFrame(data2, columns=["state", "tot_death"])

# Casting column elements as integers
df['tot_death']=df['tot_death'].astype(int)
df2['tot_death']=df2['tot_death'].astype(int)

# Sorting the dataframe entries by states so the plot appears from left to right on the plot based on the alphabetical
# arrangement of the state names.

df = df.sort_values(by=['state'])
df2 = df2.sort_values(by=['state'])

# Labelling the legends
label1 = day1 + "th " + actual_month1 + ", " +  year1
label2 = day2 + "th " + actual_month2 + ", " +  year2

# Defining the axis
X = df['state'].tolist()
x_axis = np.arange(len(X))
plt.bar(x_axis - 0.2, df['tot_death'], 0.4, label = label1)
plt.bar(x_axis + 0.2, df2['tot_death'], 0.4, label = label2)
plt.xticks(x_axis, X)

# Other details, labelling and title etc.
plt.xlabel("US State")
plt.ylabel("Deaths")
plt.legend()
plt.title("Recorded deaths from COVID-19 across the 10 most populous US States")

# Making the exact figures visible above the bar chart
r = df['tot_death']
k = df2['tot_death']
xlocs, xlabs = plt.xticks()
for i, v in enumerate(r):
    plt.text(xlocs[i] - 0.40, v + 0.31, str(v))
for i, v in enumerate(k):
    plt.text(xlocs[i] - 0.10, v + 1.1, str(v))


plt.show()



