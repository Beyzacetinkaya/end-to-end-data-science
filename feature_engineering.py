import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("user_data.csv")
df['signup_date'] = pd.to_datetime(df['signup_date'])
df['account_age_days'] = (pd.to_datetime('2024-05-28') - df['signup_date']).dt.days
df = pd.get_dummies(df, columns=['country'])
scaler = StandardScaler()
df['total_purchases_scaled'] = scaler.fit_transform(df[['total_purchases']])
print(df.head())