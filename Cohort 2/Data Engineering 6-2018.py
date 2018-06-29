# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:06:35 2018

@author: mashk
"""
#%%
# multilevel indexing and tidying

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
# tidied data
# MuliIndex 

tips = sns.load_dataset('tips')

# can aggregate
tips_smoker = tips.groupby('smoker').mean()
tips_smoker

tips_smoker.index
tips_smoker.reset_index()

tips_smoker_time = tips.groupby(['smoker','time']).mean()
tips_smoker_time
tips_smoker_time.index

tips_smoker_time.swaplevel()
tips_smoker_time.unstack()
tips_smoker_time.unstack(level = 0)

tips_size = tips.groupby(['size', 'time']).mean()
tips_size

tips_count = tips.groupby(['size', 'time']).size()
tips_count

tips_size_smoker = tips.groupby(['size', 'smoker']).size()
tips_size_smoker
# explain what is size

tips_smoker_time.swaplevel()
tips_smoker_time.unstack()
tips_smoker_time.unstack(level = 0)

tips.describe()
tips.values


#%%
# messy data

pew_raw = pd.read_csv('D:\\Acuity\\D2D\\Data Science Training\\Python\\pew_raw.csv')

pew_long = pd.melt(pew_raw,
                       ["religion"],
                       var_name="income",
                       value_name="count")
pew_long = pew_long.sort_values(by=["religion"])
pew_long.head(10)

pew_avg_cat = pd.read_csv('D:\\Acuity\\D2D\\Data Science Training\\Python\\pew_avg_cat.csv')

pew_long_avg = pd.melt(pew_avg_cat,
                       ["religion"],
                       var_name="avg.income",
                       value_name="count")

pew_long_religion = pew_long_avg.groupby('religion')

pew_long_avg = pew_long_avg.sort_values(by=["religion"])
pew_long_avg.head(10)

pew_long_religion = pew_long_avg.groupby(['religion'])
pew_long_religion.head(10)

# pew_avg = pd.Series([5, 10, 15, 25, 35, 45, 62.5])

sns.pairplot(pew_raw)

plt.figure(figsize = (16, 12))
sns.swarmplot(x = 'religion', y = '$40-50k', data = pew_raw)


#%%
# Reshape by pivoting

DateVarValRaw = pd.read_csv('D:\\Acuity\\D2D\\Data Science Training\\Python\\DataVariableValue.csv')

DateVarValPiv = DateVarValRaw.pivot(index='date', columns='variable', values='value')
