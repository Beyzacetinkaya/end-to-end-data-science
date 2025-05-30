import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("user_data.csv")
sns.histplot(df['age'], kde=True)
plt.title("Age Distribution")
plt.show()