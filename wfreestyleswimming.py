'''Chapter 1 Exercise'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("wfreestyle1500meterwr.xlsx",sheet_name="Sheet1")
df['Days'] = df['Date'].diff().dt.days # built in python way
df['Date_Labels'] = df['Date'].dt.strftime('%Y-%m-%d')
sns.set_theme(style='whitegrid')
plt.figure(figsize=(14,6))

sns.barplot(x='Date_Labels', y='Days', data=df, color='royalblue')

plt.title('Days Elapsed Between Women\'s Freestyle 1500 meter World Record Setting', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Days', fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
