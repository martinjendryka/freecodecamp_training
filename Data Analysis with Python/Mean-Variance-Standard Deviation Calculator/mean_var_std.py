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
    # convert input_list into 3x3 numpy array
    array = np.array([input_list[:3], input_list[3:6], input_list[6:]])
    
    # calculate mean, variance, std, max, min, sum
    # across rows and col and across all elements
    vals_mean =[]
    vals_mean.append(np.mean(array, axis=0).tolist()) # across rows
    vals_mean.append(np.mean(array, axis=1).tolist())  # across col
    vals_mean.append(np.mean(array))  # across all
    
    vals_var =[]
    vals_var.append(np.var(array, axis=0).tolist()) # across rows
    vals_var.append(np.var(array, axis=1).tolist())  # across col
    vals_var.append(np.var(array)) # across all
    
    vals_std= []
    vals_std.append(np.std(array, axis=0).tolist()) # across rows
    vals_std.append(np.std(array, axis=1).tolist())  # across col
    vals_std.append(np.std(array))  # across all
    
    vals_max= []
    vals_max.append(np.max(array, axis=0).tolist())  # across rows
    vals_max.append(np.max(array, axis=1).tolist()) # across col
    vals_max.append(np.max(array))  # across all
    
    vals_min = []
    vals_min.append(np.mean(array, axis=0).tolist())  # across rows
    vals_min.append(np.mean(array, axis=1).tolist())  # across col
    vals_min.append(np.mean(array))  # across all

    vals_sum = []
    vals_sum.append(np.sum(array, axis=0).tolist()) # across rows
    vals_sum.append(np.sum(array, axis=1).tolist())   # across col
    vals_sum.append(np.sum(array))   # across all

    # convert into dict
    dict = {}
    keys = ('mean','var','standard deviation','max','min','sum')
    vals = (vals_mean,vals_var,vals_std,vals_max,vals_min,vals_sum)
    for val,key in zip(vals,keys):
        dict[key] = val
        
    return dict