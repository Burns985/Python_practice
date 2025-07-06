import pandas as pd

headers = ['Account ID', 'Transaction Date', 'Transaction Amount']

data = [
    ['101', '3/2/2018', 10],
    ['101', '3/3/2018', 20],
    ['101', '3/7/2018', 30],
    ['101', '3/8/2018', 40],
    ['102', '3/5/2018', 10],
    ['102', '3/6/2018', 20],
    ['102', '3/7/2018', 30],
    ['102', '3/8/2018', 40],
    ['102', '3/20/2018', 50]
]

# Convert data to a pandas DataFrame
df = pd.DataFrame(data, columns=headers)
df['Transaction Amount'] = df['Transaction Amount'].astype(int)

rolling_averages = []

for account_id, group in df.groupby('Account ID'):
    rolling_avg_func = lambda x: x.rolling(window=3, min_periods=1).mean()
    group['Transaction Date'] = pd.to_datetime(group['Transaction Date'])
    group = group.sort_values('Transaction Date')
    group['Rolling Average'] = group['Transaction Amount'].transform(rolling_avg_func)
    rolling_averages.append(group[['Account ID', 'Transaction Date', 'Rolling Average']].to_dict('records'))

for account_averages in rolling_averages:
    print("Account ID:", account_averages[0]['Account ID'])
    for average in account_averages[-3:]:
        formatted_date = average['Transaction Date'].strftime('%Y-%m-%d')
        print("Date:", formatted_date, "Rolling Average:", average['Rolling Average'])
