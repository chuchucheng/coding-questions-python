# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:28:34 2019

@author: ccc32
"""

def build_profile(first, last, age='', **user_info):
    '''create a dictionary, all about user'''
    profile = {}
    profile['first'] = first
    profile['last'] = last
    if age:
        profile['age'] = age  # age is optional
    for key, value in user_info.items():
        profile[key] = value 
    return profile
