# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:39:13 2020

@author: User
"""

import pickle

with open('config.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
print(loaded_data)


