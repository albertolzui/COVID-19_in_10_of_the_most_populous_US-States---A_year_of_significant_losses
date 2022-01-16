#!/usr/bin/env python

# make sure to install these packages before running:
#pip install pandas
#pip install sodapy

import pandas as pd
from sodapy import Socrata
import matplotlib.pyplot as plt
from title_cal import get_month

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

result_1 = results_df.drop(columns=["consent_cases", "consent_deaths", "prob_cases", "pnew_case", "pnew_death",
                                    "prob_death", "conf_cases", "conf_death", "created_at", "new_case", "new_death",
                                    "tot_cases"])

data = result_1[result_1['submission_date']=='2021-02-12T00:00:00.000']
date_fetcher = data.iloc[[0],[0]]
date_refiner = date_fetcher.iloc[0]
date_format = date_refiner.submission_date
actual_date = date_format.replace("T00:00:00.000", "")
year = actual_date[0:4]
month = actual_date[5:7]
day = actual_date[8:]
actual_month = get_month(month)

df = pd.DataFrame(data, columns=["state", "tot_death"])
df['tot_death']=df['tot_death'].astype(int)
df = df.sort_values(by=['state'])
ax = df.plot(x="state", y="tot_death", kind="bar")
plt.xlabel("US State")
plt.ylabel("Deaths")
plt.legend(["Total deaths recorded"])
plt.title("Total number of recorded deaths from COVID-19 cases across 60 US States on the " + day + "th of " + actual_month + ", " + year + "." )

"""
#print(X)
#ax = df.plot(x="state", y="tot_death", kind="bar")
#ax2 = df2.plot(x="state", y="tot_death", kind="bar")
#plt.legend(["Total deaths recorded"], loc=9, frameon=False)
r = df['tot_death']
xlocs, xlabs = plt.xticks()
for i, v in enumerate(r):
    if v > 45000:
        plt.text(xlocs[i] - 0.95, v + 0.91, str(v))
        
"""

plt.show()


