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

################ String indexing and concatenation ###############
alphabet ='abcdefghijklmnopqrstuvwxyz'       
        
def encrypt(text, key):
  
    result = ''

    # Fill in the blanks to create an encrypted text
    for char in text.lower():
        idx = (alphabet.index(char) + key) % len(alphabet)
        # for decription: idx = alphabet.index(char) - key
        result = result + alphabet[idx]

    return result

# Check the encryption function with the shift equals to 2
print(encrypt("datacamp", 2))    

################ String ###############
text ='StRing ObJeCts haVe mANy inTEResting pROPerTies'
# Create a word list from the string stored in 'text'
word_list = text.split()

# Make every other word uppercased; otherwise - lowercased
for i in range(len(word_list)):
    if (i + 1) % 2 == 0:
        word_list[i] = word_list[i].upper()
    else:
        word_list[i] = word_list[i].lower()
        
# Join the words back and form a new string
new_text = ' '.join(word_list)
print(new_text)

# fix string errors
import pandas as pd
heroes = {'Hair color':['No Hair','BLOND','BLACK'],'Gender':['Fmale','male','Fmale']}
heroes = pd.DataFrame(heroes)
# Make all the values in the 'Hair color' column lowercased
heroes['Hair color'] = heroes['Hair color'].str.lower()
  
# Check the values in the 'Hair color' column
print(heroes['Hair color'].value_counts())

# Substitute 'Fmale' with 'Female' in the 'Gender' column
heroes["Gender"] = heroes['Gender'].str.replace('Fmale','Female')

# Check if there is no occurences of 'Fmale'
print(heroes['Gender'].value_counts())


################ regular expression ###############
import re

text = "Let's consider the following temperatures using the Celsius scale: +23 C, 0 C, -20.0 C, -2.2 C, -5.65 C, 0.0001 C. To convert them to the Fahrenheit scale you have multiply the number by 9/5 and add 32 to the result. Therefore, the corresponding temperatures in the Fahrenheit scale will be: +73.4 F, 32 F, -4.0 F, +28.04 F, 21.83 F, +32.00018 F."

# Define the pattern to search for valid temperatures
pattern = re.compile(r'[+-]?\d+\.?\d* [CF]')

# Print the temperatures out
print(re.findall(pattern, text))

# Create an object storing the matches using 'finditer()'
matches_storage = re.finditer(pattern, text)

# Loop over matches_storage and print out item properties
for match in matches_storage:
    print('matching sequence = ' + match.group())
    print('start index = ' + str(match.start()))
    print('end index = ' + str(match.end()))
    
    
pattern = re.compile(r'[A-Z][a-z]+\s[1-3]?\d,\s\d+')
text = 'Oct 23, 2000; Feb 25, 1999; which to print'

re.findall(pattern,text)



text ='Python has 4 main data structures: list, tuple, set, and dictionary.'
# Compile the regular expression
pattern = re.compile(r'[,:\.\s]+')

# Split the text that only words or numbers are left
words = re.split(pattern, text)
print(words)

# Define an easier way to extract words or numbers
alt_pattern = re.compile(r'[A-Za-z\d]+')
print(re.findall(alt_pattern, text))


################  Iterable ###############

def retrieve_character_indices(string):
    character_indices = dict()
    # Define the 'for' loop
    for index, character in enumerate(string):
        # Update the dictionary if the key already exists
        if character in character_indices:
            character_indices[character].append(index)
        # Update the dictionary if the key is absent
        else:
            character_indices[character] = [index]
            
    return character_indices
  
print(retrieve_character_indices('enumerate an Iterable'))



column_counts = dict()
# Traverse through the columns in the heroes DataFrame
for column_name, series in heroes.iteritems():
    # Retrieve the values stored in series in a list form
    values = list(series)
    category_counts = dict()  
    # Traverse through unique categories in values
    for category in set(values):
        # Count the appearance of category in values
        category_counts[category] = values.count(category)
    
    column_counts[column_name] = category_counts
    
print(column_counts)

################ List comprehension ###############
spam = 'Dear User, Our Administration Team needs to inform you that you are reaching the storage limit of your Mailbox account.\nYou have to verify your account within the next 24 hours.\nOtherwise, it will not be possible to use the service.\nPlease, click on the link below to verify your account and continue using our service. Your Administration Team.'
def create_word_list(string):
    # Finding all the words
    pattern = re.compile(r'\w+')
    words = re.findall(pattern, string)
    return words

# Convert the text to lower case and create a word list
words = create_word_list(spam.lower())

# Create a set storing only unique words
word_set = set(words)

# Create a dictionary that counts each word in the list
tuples = [(word, words.count(word)) for word in word_set]
word_counter = dict(tuples)

# Printing words that appear more than once
for (key, value) in word_counter.items():
    if value > 1:
        print("{}: {}".format(key, value))
        
################ prime number ###############
import math


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


