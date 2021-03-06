import pandas as pd
import matplotlib.pyplot as plt


dt = pd.read_csv('train.csv')
colors = ["peachpuff", "olive","brown", "coral"]

# Мне кажется, это какое-то извращение... Но самостоятельно не смогла разобраться, как по-нормальному сменить
# сразу все значения индексов. Или указать, чтобы у = 'pos' был.
dt = dt.rename(index=lambda s: s + 279)


dt.loc[:,['A','C','T', 'G']].plot.bar(stacked=True, color=colors, figsize=(10,7))
plt.title('Nucleotide distribution', fontsize=15)
plt.xlabel('Position', fontsize=10)
plt.ylabel('Nucleotide frequency', fontsize=10)
plt.savefig('bar')








