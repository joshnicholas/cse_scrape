import pandas as pd
import datetime 

today = datetime.datetime.now()
yest = today - datetime.timedelta(days=20)
yest = datetime.datetime.strftime(yest, "%Y-%m-%d")

cse = pd.read_csv('cse.csv')
# 'Company Name', 'Symbol', 'Share Volume', 'Trade Volume', 'Previous Close (Rs.)', 
# 'Open (Rs.)', 'High (Rs.)', 
# 'Low (Rs.)', '**Last Trade (Rs.)', 'Change(Rs)', 'Change Percentage (%)', 'Date'
cse = cse.loc[cse['Date'] == yest]

p = cse

print(p)
print(p.columns.tolist())
# print(yest)

with open(f'daily_dumps/{yest}.csv', 'w') as f:
    cse.to_csv(f, index=False, header=True)
