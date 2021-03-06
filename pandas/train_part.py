import pandas as pd

df = pd.read_csv('train.csv')

mean = df['matches'].sum()/len(df['matches'])
df = df.query(' matches > @mean')
print(df)
df1 = df[['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']]
print(df1)

df1.to_csv('train_part.csv', index = False)

dt = pd.read_csv('train_part.csv')
print(dt)