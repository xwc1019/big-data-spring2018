import pandas as pd
import numpy as np
import os

os.chdir('week-03')

df = pd.DataFrame()

df['name'] =['Joey','Jeremy','Wencong']

df

df.assign(age=[22,23,24])
df.assign(score=["A","B","C"])

df = pd.read_csv('data/skyhook_2017-07.csv',sep=',')

df.head()

df.dtypes

df.shape

df.shape[0]
df.shape[1]

df.columns
type(df.columns)
df.cat_name
df.cat
df.cat_name
df.count

df['count']

df.lat.unique()

df_multitpleColumns = df[['hour','cat','count']]
df_multitpleColumns.head()

df['hour'] == 158

time = df[df['hour'] == 158]
time.head
time.shape

df[(df['hour']== 158) & (df['count'] > 50)]
bastille = df[df['date'] == '2017-07-14']
bastille.head()

bastille_enthusiasts = bastille[bastille['count'] > bastille['count'].mean()]

bastille_enthusiasts.head

bastille_enthusiasts['count'].describe()

df.groupby(['date'])['count'].describe()

df.groupby(['date','hour'])['count'].describe()
df['count'].max()
df['count'].min()
df['count'].mean()
df['count'].std()
df['count'].count()

max_count = df['count'].max()
min_count = df['count'].min()
mean_count = df['count'].mean()

print(f"Maximun number of GPS pings: {max_count}")
print(f"minimum number of GPS pings: {min_count}")

print(f"mean number of GPS pings: {mean_count}")
df[df['count'] == df['count'].max()]
df[df['count'] == df['count'].min()]

df2 = df.groupby(['hour'])['count'].describe()
df2_min = df2[df2['count'] == df2['count'].min()]
df2_min

df2_count = df2['count'].min()
df2_hour = df2[df2_min[1]
print(f"The hour 50 is the hour with minimum count which is {df2_min['count']}")

df2_max = df2[df2['count'] == df2['count'].max()]
df2_max

df3 = df.groupby(['hour'])['count'].describe()

df3
df1 = df['hour'].describe()
df1
df['hour'].count()
df1 = df.mean(df['count'].mean(),df['hour'].mean())

df_sum = np.sum(df['hour'])
df_sum2 = np.sum(df['count'])
df_sum
df_ave = np.mean(df_sum2,df_sum)
df_ave = df[np.sum(['count']),mp.sum['df2_hour']].mean()
df_ave = df_sum2/df_sum
df_ave

import matplotlib
%matplotlib

day_hours = df[df['date'] == '2017-07-02'].groupby('hour')['count'].sum()
day_hours.plot()

df['date_new'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

df['date'].head

df['weekday'] = df['date_new'].apply(lambda x: x.weekday() +1)
df['weekday'].replace(7,0,inplace = True)

df['date_new'].head()

df["hour"].head

df['hours'].head

for i in range(0,168,24):
    j = range (0,168,1)[i -5]
    if (j > i):
        df.drop(df[(df['weekday'] == (i/24)) & (((df['hour'] < j) & (df['hour'] > i +18))|((df['hour'] > i + 18) & (df['hour'] <j)))].index, inplace = True)
    else:
        df.drop(df[(df['weekday'] == (i/24)) & ((df['hour'] < j) | (df['hour'] > i +18))].index,inplace = True)

df.shape

df.to_csv('data/skyhook_cleaned.csv')
