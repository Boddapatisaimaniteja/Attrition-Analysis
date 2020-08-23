# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:48:45 2020

@author: bodda
"""


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



data=pd.read_csv('E:/letsupgrade AI_ML/day 11/general_data.csv')
data=data.drop_duplicates()


#checking for null values

print(data.isnull().sum())

data=data.dropna(axis=0)
print(data.columns)
print(data.isnull().sum())
print(data.dtypes)
print(data.describe())

# Reassign target
data.Attrition.replace(to_replace = dict(Yes = 1, No = 0), inplace = True)
# Drop useless feat
data = data.drop(columns=['StandardHours', 
                          'EmployeeCount', 
                          'Over18','EmployeeID'
                        ])
print(data.head())

#H0:there is no relationship between the department and attrition
#H1:there is  relationship between the department and attrition
chitable=pd.crosstab(data.Attrition,data.Department)
from scipy.stats import chi2_contingency
stats,p,df,exception=chi2_contingency(chitable)
#inference :since p<0.05,we can reject null hypothesis i.e. attrition is taking in all departments

