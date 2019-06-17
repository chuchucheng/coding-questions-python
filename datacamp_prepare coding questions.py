# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:18:23 2019

@author: ccc
"""

################ List methods ###############

basket1 =['banana', 'kiwifruits', 'grapefruits', 'apples', 'apricots', 'nectarines', 'oranges', 'peaches', 'pears', 'lemons']
basket2 =['apples', 'grapes', 'apricots', 'dragonfruits', 'peaches', 'pears', 'limes', 'papaya']

# Remove fruits from basket2 that are present in basket1
for item in basket1:
    if item in basket2:
        basket2.remove(item)

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))

# Transfer fruits from basket1 to basket2 to make them length approximately equal
while len(basket2)<len(basket1):
    item_to_transfer = basket1.pop()
    basket2.append(item_to_transfer)

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))

################ Operations on sets ###############
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 7, 9, 11, 13, 15}
C = {1, 2, 8, 10, 11, 12, 13, 14, 15, 16, 17}
D = {1, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
E = {9, 10, 11, 12, 13, 14, 15}

A.union(B.intersection(C)) - D.intersection(E)



################ Store dictionary  ###############
range_x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
range_y = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

circ_parab = dict()

for x in range_x:
    for y in range_y:       
        # Calculate the value for z
        z = x**2 + y**2
        # Create a new key for the dictionary
        # key = (x, y)
        # Create a new key-value pair      
        circ_parab[(x, y)] = z
        
        circ_parab[(1.8,1.4)]

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############

################  ###############


