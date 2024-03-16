#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:03:04 2024

@author: martinjendryka
"""
import numpy as np
def calculate(input_list):
    if len(input_list)<9:
        raise ValueError('List must contain nine numbers.')
    # convert list into 3x3 numpy array
    array = np.array([input_list[:3], input_list[3:6], input_list[6:]])
    
    # calculate mean, variance, std, max, min, sum
    # across rows and col and across all elements
    vals_mean =[]
    vals_mean.append(array.mean(axis=0).tolist()) # across rows
    vals_mean.append(array.mean(axis=1).tolist())  # across col
    vals_mean.append(array.mean())  # across all
    
    vals_var =[]
    vals_var.append(array.var(axis=0).tolist()) # across rows
    vals_var.append(array.var(axis=1).tolist())  # across col
    vals_var.append(array.var()) # across all
    
    vals_std= []
    vals_std.append(array.std(axis=0).tolist()) # across rows
    vals_std.append(array.std(axis=1).tolist())  # across col
    vals_std.append(array.std())  # across all
    
    vals_max= []
    vals_max.append(array.max(axis=0).tolist())  # across rows
    vals_max.append(array.max(axis=1).tolist()) # across col
    vals_max.append(array.max())  # across all
    
    vals_min = []
    vals_min.append(array.min( axis=0).tolist())  # across rows
    vals_min.append(array.min( axis=1).tolist())  # across col
    vals_min.append(array.min())  # across all

    vals_sum = []
    vals_sum.append(array.sum( axis=0).tolist()) # across rows
    vals_sum.append(array.sum( axis=1).tolist())   # across col
    vals_sum.append(array.sum())   # across all

    # convert into dict
    calculations = {}
    keys = ('mean','variance','standard deviation','max','min','sum')
    vals = (vals_mean,vals_var,vals_std,vals_max,vals_min,vals_sum)
    for val,key in zip(vals,keys):
        calculations[key] = val
        
    return calculations