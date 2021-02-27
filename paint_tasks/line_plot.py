import pandas as pd
import matplotlib.pyplot as plt
# Вообще я очень хотела нарисавать какой-нибудь интересный график, взяв данные с Kggle, но чет сложно было найти такие данные,
# чтобы этот line plot не выглядел как какой-то шайтан. Поэтому взяла чисто какой-то коротенький примерчие из головы :)

Data = {'Months_of_study_at_IB': ['Sept', 'Oct', 'Nov', 'Dec','Jan' ,'Feb'],
        'liters_of_coffee_I_drank': [9.8, 12, 8, 6.5, 2.1, 6.2]
        }

df = pd.DataFrame(Data, columns=['Months_of_study_at_IB', 'liters_of_coffee_I_drank'])
print(df)
x = df['Months_of_study_at_IB']
y = df['liters_of_coffee_I_drank']

plt.title('Coffee consumption', fontsize=17)
plt.xlabel('Months of study at IB', fontsize=14)
plt.ylabel('liters of coffee I drank', fontsize=14)
plt.plot(x,y)
plt.savefig('line_chart')