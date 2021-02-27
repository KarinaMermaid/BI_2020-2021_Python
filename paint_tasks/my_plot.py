import matplotlib.pyplot as plt
import pandas as pd
path = '/home/karina_mermaid/PycharmProjects/pythonProject/paint/avocado.csv'

df = pd.read_csv(path)
df = df.rename(columns = {'Total Volume': 'Total_Volume'})
# print(df.head())
# print(df.columns)
AveragePrice = df.AveragePrice
Total_Volume = df.Total_Volume

df = df.groupby("region").last()
df = df.iloc[10:]
print(df)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)


ax1.violinplot(df.AveragePrice, showmedians=True)
ax1.set_title('AveragePrice')

ax2.violinplot(df.Total_Volume, showmedians=True)
ax2.set_title('Total_Volume')

plt.savefig('Violin Plot')