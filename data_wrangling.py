import pandas as pd
df = pd.read_csv("user_data.csv")
df['signup_date'] = pd.to_datetime(df['signup_date'])
df['last_login'] = pd.to_datetime(df['last_login'])
df['days_since_last_login'] = (pd.to_datetime('2024-05-28') - df['last_login']).dt.days
df.fillna(0, inplace=True)
print(df.head())