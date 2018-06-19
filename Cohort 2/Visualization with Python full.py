# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:01:43 2018

@author: mashk
"""
#%%


#import modules
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Matplotlib default settings
print(plt.rcParams)

# set matplotlib style
# https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html

from matplotlib import style
style.use('ggplot')
#style.use('classic')  seaborn-bright
# style.use('seaborn-bright')

#import data
tips = sns.load_dataset('tips')
tips.head()

iris = sns.load_dataset('iris')

plt.figure(figsize = (5, 6))

#%%

## matplotlib basic 
# multiple line on one plot

plt.plot(tips['tip'])
plt.plot(tips['total_bill'])

# plot size
plt.figure(figsize = (12, 8))
plt.plot(tips['tip'])
plt.plot(tips['total_bill'])

# axis
plt.figure(figsize = (12, 8))
plt.plot(tips['tip'])
plt.plot(tips['total_bill'])
plt.ylabel('Dollars')
plt.xlabel('Bill Number')

# legend
plt.figure(figsize = (12, 8))
plt.plot(tips['tip'])
plt.plot(tips['total_bill'])
plt.ylabel('Dollars')
plt.xlabel('Bill Number')
plt.legend(loc = 'best')

# explore relations
plt.plot(tips['total_bill'], tips['tip'], marker = '.', linestyle = 'None')


# perform some EDA w/ seaborn

sns.pairplot(tips)
sns.pairplot(tips, kind = 'reg')
sns.pairplot(tips, kind = 'reg', hue = 'sex')
sns.pairplot(tips, kind = 'reg', hue = 'smoker')
sns.pairplot(tips, kind = 'reg', hue = 'time')
sns.pairplot(tips, kind = 'reg', hue = 'size')

# boxplot
sns.boxplot(x="day", y="total_bill", data=tips)
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set3")
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips, palette="Set3")
sns.boxplot(x="day", y="total_bill", hue="day", data=tips, linewidth = 2.5)

# boxplot with swarmplot
sns.boxplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", data=tips, color=".25")

# boxplot with specific order
sns.boxplot(x = "time", y = "total_bill", data = tips, order = ["Dinner", "Lunch"])

# factorplot
sns.factorplot(x="sex", y="total_bill", hue="smoker", col="time", data=tips, kind="box", size=4, aspect=.7)

# add a colunm
tips['tip_percent'] = tips['tip'] / tips['total_bill'] * 100

sns.pairplot(tips, diag_kind = 'kde')

tipsMale = tips[tips['sex'].str.contains('Male')]
tipsFemale = tips[tips['sex'].str.contains('Female')]

sns.jointplot(y = 'tip', x = 'total_bill', data = tips)
sns.jointplot(y = 'tip_percent', x = 'total_bill', data = tips)

sns.regplot(y = 'tip_percent', x = 'total_bill', data = tips, color = 'green')
sns.regplot(y = 'tip_percent', x = 'total_bill', data = tips, order = 2, color = 'red')

plt.scatter(y = 'tip_percent', x = 'total_bill', data = tips, color = 'grey')
sns.regplot(y = 'tip_percent', x = 'total_bill', data = tips, color = 'green', scatter = None)
sns.regplot(y = 'tip_percent', x = 'total_bill', data = tips, order = 2, color = 'red', scatter = None)



#%%
# seaborn color palettes
# https://seaborn.pydata.org/tutorial/color_palettes.html

current_palette = sns.color_palette()
sns.palplot(current_palette)


sns.pairplot(tips, kind = 'reg', hue = 'sex')
sns.pairplot(tips, kind = 'reg', hue = 'sex', palette = 'Set1')
sns.pairplot(tips, kind = 'reg', hue = 'sex', palette = 'Paired')


#%% 
# strip,swarm,and violin plots

# remember the iris data
sns.pairplot(iris)
sns.pairplot(iris, kind = 'reg')
sns.pairplot(iris, kind = 'reg', hue = 'species') # group by Species

# sns strip plot
sns.stripplot(x = 'species', y = 'petal_length', data = iris)
# + jitter
sns.stripplot(x = 'species', y = 'petal_length', data = iris, jitter = True, size = 5)
sns.stripplot(x = 'species', y = 'petal_length', data = iris, hue = 'species', jitter = True, size = 5)

# sns swarpplot
sns.swarmplot(x = 'species', y = 'petal_length', data = iris, hue = 'species')

# sns violin  and strip plots plot
sns.violinplot(x = 'species', y = 'petal_length', data = iris)
sns.violinplot(x = 'species', y = 'petal_length', data = iris, inner = None)
sns.violinplot(x = 'species', y = 'petal_length', data = iris, inner = None, color = 'lightgray')

sns.violinplot(x = 'species', y = 'petal_length', data = iris, inner = None, color = 'lightgray')
sns.stripplot(x = 'species', y = 'petal_length', data = iris, hue = 'species', jitter = True, size = 5)

# joint distribution 
sns.jointplot(x = 'petal_length', y = 'petal_width', data = iris)
sns.jointplot(x = 'petal_length', y = 'petal_width', data = iris, kind = 'reg')
sns.jointplot(x = 'petal_length', y = 'petal_width', data = iris, kind = 'kde')

sns.jointplot(x = 'petal_length', y = 'petal_width', data = iris, kind = 'hex')
plt.colorbar()

# box plot 

sns.boxplot(x = 'petal_length', y = 'species', data = iris)
sns.boxplot(y = 'petal_length', x = 'species', data = iris)

sns.boxplot(x="day", y="total_bill", data=tips)
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set3")
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips, palette="Set3")

#%%

#%%
# seaborn regressions

sns.lmplot(y = 'tip_percent', x = 'tip', data = tips)
sns.residplot(y = 'tip_percent', x = 'tip', data = tips)

sns.lmplot(y = 'tip_percent', x = 'tip', data = tips, hue = 'sex')

sns.regplot(y = 'tip_percent', x = 'tip', data = tips, order = 2)

sns.regplot(y = 'tip_percent', x = 'tip', data = tips, color = 'red')
sns.regplot(y = 'tip_percent', x = 'tip', data = tips, scatter = None, order = 2, color = 'green')
sns.regplot(y = 'tip_percent', x = 'tip', data = tips, scatter = None, order = 3, color = 'blue')
# order = 3 is overfitting

# different colors for samples and reg lines

plt.plot(tips['tip'], tips['tip_percent'], color = 'grey', marker = '.', linestyle = 'None') 
# note different syntax in plt and sns
sns.regplot(y = 'tip_percent', x = 'tip', data = tips, scatter = None, color = 'red')
sns.regplot(y = 'tip_percent', x = 'tip', data = tips, scatter = None, order = 2, color = 'green')
sns.regplot(y = 'tip_percent', x = 'tip', data = tips, scatter = None, order = 3, color = 'blue')
# order = 3 is overfitting

# group regressions by hue
sns.lmplot(y = 'tip_percent', x = 'tip', data = tips, hue = 'sex')

# group regressions by row (column)
sns.lmplot(y = 'tip_percent', x = 'tip', data = tips, row = 'sex')

#%%
# subplot()

plt.subplot(2,1,1)  # two rows, one column, the one on top is active
sns.stripplot(x = 'species', y = 'petal_length', data = iris)
plt.subplot(2,1,2)  # bottom one is active 
sns.stripplot(x = 'species', y = 'petal_length', data = iris, jitter = True, size = 5)

plt.figure(figsize = (16, 12))
plt.subplot(2,2,1)  # two rows, two columna, the left on top is active
sns.stripplot(x = 'species', y = 'petal_length', data = iris)
plt.subplot(2,2,2)  
sns.stripplot(x = 'species', y = 'petal_length', data = iris, jitter = True, size = 5)
plt.subplot(2,2,3)
sns.violinplot(x = 'species', y = 'petal_length', data = iris)
plt.subplot(2,2,4)
sns.violinplot(x = 'species', y = 'petal_length', data = iris, inner = None)
sns.violinplot(x = 'species', y = 'petal_length', data = iris, inner = None, color = 'lightgray')
sns.stripplot(x = 'species', y = 'petal_length', data = iris, hue = 'species', jitter = True, size = 3)


#%% 
# 2D arrays

A = np.array([[1,2,1], [0,0,1], [-1,1,1]])
plt.pcolor(A, cmap = 'Blues')

# correct
A = np.array([[1,0,-1], [2,0,1], [1,1,1]])
plt.pcolor(A, cmap = 'Blues')
plt.colorbar()

A = np.array([[-1,0,1], [1,0,2], [1,1,1]])
plt.pcolor(A, cmap = 'Blues')

A = np.array([[1,1,1], [2,0,1], [1,0,-1]])
plt.pcolor(A, cmap = 'Blues')

#%%
# meshes

u = np.linspace(-2, 2, 65)
v = np.linspace(-1, 1, 33)
X, Y = np.meshgrid(u, v)
Z = X ** 2 / 25 + Y **2 / 4
# plt.colormaps()

# plt.pcolor(X, Y, Z) # X, Y values on axes
plt.pcolor(Z) # sample number on axes
plt.colorbar()

plt.contour(Z, 25)
plt.colorbar()

plt.contour(X, Y, Z, 25)
plt.colorbar()

plt.contourf(X, Y, Z, 25)  # filled contour plot
plt.colorbar()

u = np.linspace(-2, 2, num = 41)
v = np.linspace(-1, 1, num = 21)
X, Y = np.meshgrid(u, v)
Z = np.sin(3* np.sqrt(X**2 + Y**2))

plt.set_cmap('gray')  ## not 'grey'!
plt.pcolor(Z)

plt.set_cmap('viridis')
plt.contour(X, Y, Z)

#%%
# 2d histograms

plt.hist2d('total_bill', 'tip', data = tips, bins = (20, 10))
plt.colorbar()

plt.hexbin('total_bill', 'tip', data = tips, gridsize = (20, 10))
plt.colorbar()

#%%
# covariance / correlation w/ heatmap

covIris = iris.cov() 
print(covIris)

plt.figure(figsize = (12, 8))
sns.heatmap(covIris)

covTips = tips.cov() 
print(covTips)

plt.figure(figsize = (12, 8))
sns.heatmap(covTips)

corrIris = iris.corr() 
print(corrIris)

plt.figure(figsize = (12, 8))
sns.heatmap(corrIris)

corrTips = tips.corr() 
print(corrTips)

plt.figure(figsize = (12, 8))
sns.heatmap(corrTips)


