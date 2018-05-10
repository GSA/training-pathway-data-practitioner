# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:17:39 2018

@author: mashk
"""

#%%
# def load_iris(return_X_y=False):

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfIris = pd.read_csv('D:\\Acuity\\D2D\\Data Science Training\\Python\\Iris.csv')
npIris = np.genfromtxt('D:\\Acuity\\D2D\\Data Science Training\\Python\\Iris.csv', delimiter=',')
versicolor = npIris[51:101]
versPetalLength = versicolor[:, 2]

# arr = np.arange(1, 51)

# delete first row
# npIrisD = np.delete(npIris, (0), axis = 0)
# delete 4th column
# npIrisDD = np.delete(npIrisD, (4), axis = 1)

print(npIris)

print(dfIris)
print(dfIris.as_matrix(columns=dfIris.columns[2:3]))

print(npIris[:,3])


# histograms
plt.hist('Sepal.Length', data = dfIris, bins = 5)
plt.hist('Sepal.Length', data = dfIris, bins = 10)
plt.hist('Sepal.Length', data = dfIris, bins = 20)

# scatter plots
import seaborn as sns
sns.set()
plt.plot('Sepal.Length', 'Petal.Length', marker = '.', linestyle = 'none', data = dfIris)
plt.show()

# bee swarm plot
sns.swarmplot(x = 'Species', y = 'Petal.Length', data = dfIris)

# ECDF
def ecdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n + 1) / n
    return x, y

#print()
x_vers, y_vers = ecdf(versPetalLength)
plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')
    

