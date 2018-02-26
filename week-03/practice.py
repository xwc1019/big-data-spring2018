import pandas as pd
import numpy as np
import matplotlib
new_list = []
df = pd.DataFrame()
print(df)
df['name'] = ['1','2','3']

df
df.assign(height = [0.5, 0.4, 0.6])

import os
os.chdir('week-03')
df = pd.read_csv('data/skyhook_2017-07.csv',sep=',')

df.head()

df.shape[1]

df.columns

df['cat_name'].unique()
df['count']

df['hour'] == 158
one_fifty_eight = df[df['hour'] == 158]

one_fifty_eight.shape

df[df(['hour'] == 158) & (df['count']>50)].shape

bastille = df[df['date'] == '2017-07-14']
#greater than average cells
bastille['count'] > bastille['count'].mean()

lovers_of_bastille = bastille[bastille['count'] > bastille['count'].mean()]
lovers_of_bastille.describe()

df.groupby('date')['count'].describe()
