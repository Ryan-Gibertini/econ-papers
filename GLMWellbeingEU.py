# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:19:33 2019

@author: ryang
"""

from pandas import read_csv
import numpy as np
from pandas import DataFrame
from numpy import array
import statsmodels.api as sm
data1 = read_csv('C:/Users/ryang/WellbeingEU.csv', delimiter=",")
Y = np.transpose(np.array([data1.WELL]))
X = np.transpose(np.array([data1.GDPK, data1.LIFE, data1.DD, data1.UMEPY]))
X = sm.add_constant(X)
model1 = sm.GLM(endog=Y, exog=X, family=sm.families.Poisson())
results  = model1.fit()
beta_hats = results.params
print(results.summary())
Y = np.transpose(np.array([data1.WELL]))
X = np.transpose(np.array([data1.GDPK, data1.UMEPY]))
X = sm.add_constant(X)
model1 = sm.GLM(endog=Y, exog=X, family=sm.families.Poisson())
results  = model1.fit()
beta_hats = results.params
print(results.summary())
print(np.mean(results.resid_deviance))
print(np.std(results.resid_deviance))
mean = np.mean(results.resid_deviance) 
std = np.std(results.resid_deviance)
resid = results.resid_deviance
stand_resid = (((resid) - (mean))/std)
np.mean(stand_resid)
np.std(stand_resid)
print(np.mean(stand_resid))
print(np.std(stand_resid))














