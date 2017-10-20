
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import datetime
get_ipython().magic('matplotlib inline')


# In[2]:


# Load data
T2Hfile = pd.ExcelFile('https://inventory.data.gov/dataset/58fa1cd3-c1bf-4492-964d-f994b26a6cae/resource/f6d8dd83-3080-470f-b453-03f8ead0228f/download/time-to-hire-data-file.xlsx')


# In[3]:


# Create dataframe
df = pd.DataFrame(T2Hfile.parse('TimetoHire1-15-2010 (1)'))


# In[4]:


df


# In[7]:


# First four of the job series, convert to integer and then to string
def clean(x):
    j = []
    if len(x) == 3: 
        for i in x:
                j.append(i)
        j.insert(0,'0')           
 
    else:                             
        for i in x:
            if not i.isalpha():
                j.append(i)
            else:
                break
                
    return(''.join(j))

df['SERIES'] = df['SERIES'].astype('str')
df['CLEAN_SERIES'] = df['SERIES'].apply(lambda x :clean(x))
df['CLEAN_SERIES'] = df['CLEAN_SERIES'].fillna(0)
df['CLEAN_SERIES'].unique()


# In[8]:


# Calculate time to hire dimension
df['T2H_days'] = pd.Series(delta.days for delta in (df['HIRED_DATE'] - df['RECEIVED_DATE']))

# Create year hired
df['HIRED_DATE_CY'] = df['HIRED_DATE'].dt.year.apply(str)

# subset T2H with positive values
# df = df[(df.T2H_days >= 0) & (df.HIRE_COUNT > 0)] 
df = df[(df['T2H_days'] >= 0) & (df['HIRE_COUNT'] > 0)] 
df.describe()
pd.crosstab(df.HIRED_DATE_CY, df.HIRE_COUNT, margins=True) 

### crosstab - https://chrisalbon.com/python/pandas_crosstabs.html

# subset for 1101s, 1102s
df11xxANOVA = df[(df.CLEAN_SERIES == "1101") | (df.CLEAN_SERIES == "1102")]
pd.crosstab(df11xxANOVA.CLEAN_SERIES, df11xxANOVA.HIRE_COUNT, margins=True)

df1102 = df[df.CLEAN_SERIES == "1102"]
pd.crosstab(df1102.HIRED_DATE_CY, df1102.HIRE_COUNT, margins=True)


# In[10]:


def get_financial_year(datestring):
            date = datetime.datetime.strptime(datestring, "%Y-%m-%d").date()
            #initialize the current year
            year_of_date=date.year
            #initialize the current financial year start date
            financial_year_start_date = datetime.datetime.strptime(str(year_of_date)+"-10-01","%Y-%m-%d").date()
            if date<financial_year_start_date:
                    return (financial_year_start_date.year-1)
            else:
                    return (financial_year_start_date.year)


# In[11]:


#There were some missing indexes, which was throwing my code out of whack. I had to reset index here
df = df.reset_index(drop=True)


# In[12]:


#Creates FiscalYear column
df.assign(FiscalYear = np.nan)


# In[ ]:


#Fills in FiscalYear column
count = 0
while count < df['HIRED_DATE_CY'].count():
    FY = get_financial_year(df['HIRED_DATE'][count].strftime('%Y-%m-%d'))
    df.loc[count, 'FiscalYear'] = str(FY)
    count= count +1


# In[11]:


#Creates Hired_Date_FY column
df['HIRED_DATE_FY'] = df['FiscalYear'] + '-' + df['HIRED_DATE'].dt.month.apply(str) + '-' + df['HIRED_DATE'].dt.day.apply(str)


# In[19]:


df['HIRED_DATE_FY'] = df['HIRED_DATE_FY'].str[:4]
df['HIRED_DATE_FY']


# In[18]:


#Comparison - column graph
import seaborn as sns
sns.countplot(x = 'HIRED_DATE_CY', data = df)

# seaborn.countplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, 
    # orient=None, color=None, palette=None, saturation=0.75, dodge=True, ax=None, **kwargs)

# https://seaborn.pydata.org/generated/seaborn.countplot.html


# In[21]:


sns.countplot(y = 'HIRED_DATE_CY' , data = df)


# In[9]:


#histogram-T2H Overall using pandas
sns.distplot(df['T2H_days'],kde=False)

# seaborn.distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None, hist_kws=None, 
    # kde_kws=None, rug_kws=None, fit_kws=None, color=None, vertical=False, norm_hist=False, 
    # axlabel=None, label=None, ax=None)
    
# https://seaborn.pydata.org/generated/seaborn.distplot.html


# In[101]:





# In[10]:


df1102.plot.line(x = 'HIRED_DATE', y = 'HIRE_COUNT')

# matplotlib.pyplot.acorr(x, hold=None, data=None, **kwargs)¶

# https://matplotlib.org/users/pyplot_tutorial.html
# https://matplotlib.org/api/pyplot_api.html#module-matplotlib.pyplot


# In[11]:


#box & whisker for four 1100 series jobs
#dfBox = df[(df.series_clean == "1101") | (df.series_clean == "1102") | 
    # (df.series_clean == "1170")|(df.series_clean == "1176") ]
    
sns.boxplot(x = 'CLEAN_SERIES', y = 'T2H_days',data = df[(df.CLEAN_SERIES == "1101") | (df.CLEAN_SERIES == "1102") |(df.CLEAN_SERIES == "1170")|(df.CLEAN_SERIES == "1176") ])

# Axes.boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None, patch_artist=None, 
    # bootstrap=None, usermedians=None, conf_intervals=None, meanline=None, showmeans=None, showcaps=None, 
    # showbox=None, showfliers=None, boxprops=None, labels=None, flierprops=None, medianprops=None, meanprops=None, 
    # capprops=None, whiskerprops=None, manage_xticks=True, autorange=False, zorder=None, *, data=None)
    
# https://matplotlib.org/examples/pylab_examples/boxplot_demo.html
# https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.boxplot.html


# In[12]:


# Python is not very good at handling date datatypes. 
# This converts the dates into unix time code which is the number of seconds since Jan 1st 1970.  

from datetime import datetime
import calendar 
newarr=[]

for dt64 in df1102['HIRED_DATE']:
    imadt = dt64.to_pydatetime()
    newarr.append(calendar.timegm(imadt.timetuple()))
df1102['HIRED_DATE_NDT64'] = newarr
df1102.plot.scatter(x='HIRED_DATE_NDT64',y='T2H_days' )


