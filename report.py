# -*- coding: utf-8 -*-
"""
@author: ryang
"""

from pandas import read_csv
import numpy as np
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso
from sklearn.model_selection import cross_validate
from sklearn.metrics import make_scorer

sales = read_csv('C:/Users/ryang/validation_set.csv')


# Full model
Y = np.transpose(np.array([sales.price]))
X = np.transpose(np.array([sales.year, sales.home_size, sales.parcel_size, sales.beds, sales.age, sales.pool, sales.cbd_dist, sales.x_coord, sales.y_coord]))
X=sm.add_constant(X)

print(cross_val_score(Lasso(), X, Y, cv=10))
mse = make_scorer(mean_squared_error)
mse_score=cross_val_score(Lasso(), X, Y, cv=10, scoring=mse)

scores=cross_validate(Lasso(), X, Y, cv=10, scoring=('r2', 'neg_mean_squared_error'), return_train_score=True)
print(scores['train_neg_mean_squared_error'])
print("Average CV Neg_Train_MSE:{}".format(np.mean(scores['train_neg_mean_squared_error'])))
print(scores['train_r2'])
print("Average CV Train_r2:{}".format(np.mean(scores['train_r2'])))

# Adding home_size*beds interaction
bed_home_size = sales.beds*sales.home_size
Y = np.transpose(np.array([sales.price]))
X = np.transpose(np.array([bed_home_size, sales.year, sales.home_size, sales.parcel_size, sales.beds, sales.age, sales.pool, sales.cbd_dist, sales.x_coord, sales.y_coord]))
X=sm.add_constant(X)

print(cross_val_score(Lasso(), X, Y, cv=10))
mse = make_scorer(mean_squared_error)
mse_score=cross_val_score(Lasso(), X, Y, cv=10, scoring=mse)

scores=cross_validate(Lasso(), X, Y, cv=10, scoring=('r2', 'neg_mean_squared_error'), return_train_score=True)
print(scores['train_neg_mean_squared_error'])
print("Average CV Neg_Train_MSE:{}".format(np.mean(scores['train_neg_mean_squared_error'])))
print(scores['train_r2'])
print("Average CV Train_r2:{}".format(np.mean(scores['train_r2'])))

# Adding coords interaction
coords = sales.x_coord*sales.y_coord
bed_home_size = sales.beds*sales.home_size
Y = np.transpose(np.array([sales.price]))
X = np.transpose(np.array([coords, bed_home_size, sales.year, sales.home_size, sales.parcel_size, sales.beds, sales.age, sales.pool, sales.cbd_dist, sales.x_coord, sales.y_coord]))
X=sm.add_constant(X)

print(cross_val_score(Lasso(), X, Y, cv=10))
mse = make_scorer(mean_squared_error)
mse_score=cross_val_score(Lasso(), X, Y, cv=10, scoring=mse)

scores=cross_validate(Lasso(), X, Y, cv=10, scoring=('r2', 'neg_mean_squared_error'), return_train_score=True)
print(scores['train_neg_mean_squared_error'])
print("Average CV Neg_Train_MSE:{}".format(np.mean(scores['train_neg_mean_squared_error'])))
print(scores['train_r2'])
print("Average CV Train_r2:{}".format(np.mean(scores['train_r2'])))

# Adding home size and parcel size interaction
parcel_home = sales.home_size*sales.parcel_size
coords = sales.x_coord*sales.y_coord
bed_home_size = sales.beds*sales.home_size
Y = np.transpose(np.array([sales.price]))
X = np.transpose(np.array([parcel_home, coords, bed_home_size, sales.year, sales.home_size, sales.parcel_size, sales.beds, sales.age, sales.pool, sales.cbd_dist, sales.x_coord, sales.y_coord]))
X=sm.add_constant(X)

print(cross_val_score(Lasso(), X, Y, cv=10))
mse = make_scorer(mean_squared_error)
mse_score=cross_val_score(Lasso(), X, Y, cv=10, scoring=mse)

scores=cross_validate(Lasso(), X, Y, cv=10, scoring=('r2', 'neg_mean_squared_error'), return_train_score=True)
print(scores['train_neg_mean_squared_error'])
print("Average CV Neg_Train_MSE:{}".format(np.mean(scores['train_neg_mean_squared_error'])))
print(scores['train_r2'])
print("Average CV Train_r2:{}".format(np.mean(scores['train_r2'])))

# Raising the power of the Year term
parcel_home = sales.home_size*sales.parcel_size
coords = sales.x_coord*sales.y_coord
bed_home_size = sales.beds*sales.home_size
Y = np.transpose(np.array([sales.price]))
X = np.transpose(np.array([parcel_home, coords, bed_home_size, np.power(sales.year, 2), sales.home_size, sales.parcel_size, sales.beds, sales.age, sales.pool, sales.cbd_dist, sales.x_coord, sales.y_coord]))
X=sm.add_constant(X)

print(cross_val_score(Lasso(), X, Y, cv=10))
mse = make_scorer(mean_squared_error)
mse_score=cross_val_score(Lasso(), X, Y, cv=10, scoring=mse)

scores=cross_validate(Lasso(), X, Y, cv=10, scoring=('r2', 'neg_mean_squared_error'), return_train_score=True)
print(scores['train_neg_mean_squared_error'])
print("Average CV Neg_Train_MSE:{}".format(np.mean(scores['train_neg_mean_squared_error'])))
print(scores['train_r2'])
print("Average CV Train_r2:{}".format(np.mean(scores['train_r2'])))

# One more interaction, home size and pools
home_pool = sales.home_size*sales.pool
parcel_home = sales.home_size*sales.parcel_size
coords = sales.x_coord*sales.y_coord
bed_home_size = sales.beds*sales.home_size
Y = np.transpose(np.array([sales.price]))
X = np.transpose(np.array([home_pool, parcel_home, coords, bed_home_size, np.power(sales.year, 2), sales.home_size, sales.parcel_size, sales.beds, sales.age, sales.pool, sales.cbd_dist, sales.x_coord, sales.y_coord]))
X=sm.add_constant(X)

print(cross_val_score(Lasso(), X, Y, cv=10))
mse = make_scorer(mean_squared_error)
mse_score=cross_val_score(Lasso(), X, Y, cv=10, scoring=mse)

scores=cross_validate(Lasso(), X, Y, cv=10, scoring=('r2', 'neg_mean_squared_error'), return_train_score=True)
print(scores['train_neg_mean_squared_error'])
print("Average CV Neg_Train_MSE:{}".format(np.mean(scores['train_neg_mean_squared_error'])))
print(scores['train_r2'])
print("Average CV Train_r2:{}".format(np.mean(scores['train_r2'])))

























