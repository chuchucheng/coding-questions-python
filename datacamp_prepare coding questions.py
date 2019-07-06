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

cands = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49]

def is_prime(n):
    # Define the initial check
    if n < 2:
       return False
    # Define the loop checking if a number is not prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
# Filter prime numbers into the new list
primes = [num for num in cands if is_prime(num) == True]
print("primes = " + str(primes))

################ Coprime number sequence ###############
list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
list2 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
#Two numbers a and b are coprime if their Greatest Common Divisor (GCD) is 1.
def gcd(a, b):
    # Define the while loop as described
    while b != 0:
        temp_a = a
        a = b
        b = temp_a % b   
    # Complete the return statement
    return a
    
# Create a list of tuples defining pairs of coprime numbers
coprimes = [(i,j) for i in list1 
                 for j in list2 if gcd(i,j) == 1]
print(coprimes)

################ zip ###############

wlist = [['Python', 'creativity', 'universe'],
 ['interview', 'study', 'job', 'university', 'lecture'],
 ['task', 'objective', 'aim', 'subject', 'programming', 'test', 'research']]

# Define a function searching for the longest word
def get_longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Create lists with the lengths and longest words
lengths = [len(item) for item in wlist]
words = [get_longest_word(item) for item in wlist]

# Combine the resulting data into one iterable object
for item in zip(wlist, lengths, words):
    print(item)
    
    
# Create a list of tuples with lengths and longest words
result = [
    (len(item), get_longest_word(item)) for item in wlist
]

# Unzip the result    
lengths, words = zip(*result)

for item in zip(wlist, lengths, words):
    print(item)

# Create a list of tuples with words and their lengths
word_lengths = [
    (item, len(item)) for items in wlist for item in items
]

# Unwrap the word_lengths
words, lengths = zip(*word_lengths)

# Create a zip object
col_names = ['word', 'length']
result = zip(col_names, [words, lengths])

# Convert the result to a dictionary and build a DataFrame
data_frame = pd.DataFrame(dict(result))
print(data_frame)

################ Generator ###############
def shift_string(string, shift):
    len_string = len(string)
    # Define a for loop with the yield statement
    # shift to left by x letters
    for idx in range(0, len_string):
        yield string[(idx - shift) % len_string]
       
# Create a generator
gen = shift_string('DataCamp', 5)

# Create a new string using the generator and print it out
string_shifted = ''.join(gen)
print(string_shifted)


### throw dice and calculate ratio
import random
def simulate_dice_throws():
    total, out = 0, dict([(i, [0, 0]) for i in range(1, 7)])
    while True:
        # Simulate a single toss to get a new number
        num = random.randint(1,6)
        total += 1
        # Update the number and the ratio of realizations
        out[num][0] +=1
        out[num][1] = round(out[num][0]/total, 2)
        # Yield the updated dictionary
        yield out

# Create the generator and simulate 1000 tosses
dice_simulator = simulate_dice_throws()
for i in range(1, 101):
    print(str(i) + ': ' + str(next(dice_simulator)))
    
    
    
# Rewrite func1() as a generator comprehension
def func1(n):
  for i in range(0, n):
    yield i**2
    
gen = (i**2 for i in range(0,10))

for item in zip(gen, func1(10)):
    print(item)

# Rewrite func2() as a generator comprehension
def func2(n):
  for i in range(0, n):
     if i%2 == 0:
       yield 2*i
       
gen = (2*i for i in range(0,10) if i%2 ==0)

for item in zip(gen, func2(20)):
    print(item)


# Rewrite func3() as a generator comprehension
def func3(n, m):
  for i in func1(n):
    for j in func2(m):
      yield ((i, j), i + j)
      
gen = (((i,j), i+j) for j in func2(10) for i in func1(8))

for item in zip(gen, func3(8, 10)):
    print(item)

################ functions with different argument types ###############
# Define the function with an arbitrary number of arguments
    # sort num and string
def sort_types(*args):
    nums, strings = [], []    
    for arg in args:
        # Check if 'arg' is a number and add it to 'nums'
        if isinstance(arg, (int,float)) == True:
            nums.append(arg)
        # Check if 'arg' is a string and add it to 'strings'
        elif isinstance(arg, str) == True:
            strings.append(arg)
    
    return (nums, strings)
            
print(sort_types(1.57, 'car', 'hat', 4, 5, 'tree', 0.89))




# Define the function with an arbitrary number of arguments
def key_types(**kwargs):
    dict_type = dict()
    # Iterate over key value pairs
    for key, value in kwargs.items():
        # Update a list associated with a key
        if type(value) in dict_type:
            dict_type[type(value)].append(key)
        else:
            dict_type[type(value)] = [key]
            
    return dict_type
  
res = key_types(a=1, b=2, c=(1, 2), d=3.1, e=4.2)
print(res)




# Define the arguments passed to the function
def sort_all_types(*args, **kwargs):

    # Find all the numbers and strings in the 1st argument
    nums1, strings1 = sort_types(*args)
    
    # Find all the numbers and strings in the 2nd argument
    nums2, strings2 = sort_types(*kwargs.values())
    
    return (nums1 + nums2, strings1 + strings2)
  
res = sort_all_types(
	1, 2.0, 'dog', 5.1, num1 = 0.0, num2 = 5, str1 = 'cat'
)
print(res)



################ Lambda expression ###############
# Take x and return x squared if x > 0 and 0, otherwise
squared_no_negatives = lambda x: x**2 if x>0 else 0
print(squared_no_negatives(2.0))se
print(squared_no_negatives(-1))

# Take a list of integers nums and leave only even numbers
get_even = lambda nums: [n for n in nums if n % 2 == 0]
print(get_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Take strings s1, s2 and list their common characters
common_chars = lambda s1,s2: [x for x in s1 if x in s2]
print(common_chars('pasta', 'pizza'))


import math
lambda3 = lambda *nums: math.sqrt(sum([n**2 for n in nums]))
print(str(lambda3(3, 4, 5)))




# Sort words by the string length
words.sort(key=lambda s: len(s))
print(words)

# Sort words by the last character in a string
words.sort(key=lambda s: s[-1])
print(words)

# Sort words by the total amount of certain characters
words.sort(key=lambda s: s.count('a') +s.count('b')+ s.count('c'))
print(words)

################ map filter and reduce ###############
def my_zip(*args):
    
    # Retrieve Iterable lengths and find the minimal length
    lengths = list(map(len,args))
    min_length = min(lengths)

    tuple_list = []
    for i in range(0, min_length):
        # Append new items to the 'tuple_list'
        tuple_list.append(tuple(map(lambda x:x[i],args)))

    return tuple_list

result = my_zip([1, 2, 3], ['a', 'b', 'c', 'd'], 'DataCamp')
print(result)



nums = list(range(100))
# Filter out all the numbers in nums divisible by 3 or 5
print(nums)
fnums = filter(lambda n: n%3 == 0 or n%5 ==0, nums)
print(list(fnums))


string = 'Ordinary Least Squares'
# Return the string without its vowels
print(string)
vowels = ['a','e','i','o','u']
fstring = filter(lambda word:[x for x in word if x not in vowels], string)
print(''.join(fstring))

spells = ['riddikulus',
 'obliviate',
 'sectumsempra',
 'avada kedavra',
 'alohomora',
 'lumos',
 'expelliarmus',
 'expecto patronum']
# Filter all the spells in spells with more than two 'a's
print(spells)
fspells = filter(lambda x: x.count('a') >=2, spells )
print(list(fspells))


# Reverse a string using reduce()
string = 'DataCamp'
inv_string = reduce(lambda x, y: y + x, string)
print('Inverted string = ' + inv_string) 

# Find common items shared among all the lists in lists
lists = [[1, 4, 8, 9], [2, 4, 6, 9, 10, 1], [9, 0, 1, 2, 4]]
common_items = reduce(lambda x, y: set(x).intersection(y), lists)
print('common items = ' + str(common_items))

# Convert a number sequence into a single number
nums = [5, 6, 0, 1]
num = reduce(lambda x,y: x*10+y,nums)
print(str(nums) + ' is converted to ' + str(num))


################ recursion  ###############
#Fibonacci sequence
def fib(n):

  if n < 2:
    return (n, 1)

  fib1 = fib(n-1)
  fib2 = fib(n-2)

  return (fib1[0] + fib2[0], fib1[1] + fib2[1] + 1)


# Calculate an average value of the sequence of numbers
def average(nums):
  
    # Base case
    if len(nums) == 1:  
        return nums[0]
    
    # Recursive call
    n = len(nums)
    return (nums[0] + (n - 1) * average(nums[1:])) / n  

# Testing the function
print(average([1, 2, 3, 4, 5]))


## approximate Pi
# Write an expression to get the k-th element of the series 
get_elmnt = lambda k: ((-1)**k)/(2*k+1)

def calc_pi(n):
    curr_elmnt = get_elmnt(n)
    
    # Define the base case
    if n==0:
    	return 4 
      
    # Make the recursive call
    return 4*curr_elmnt + calc_pi(n-1)
  
# Compare the approximated Pi value to the theoretical one
print("approx = {}, theor = {}".format(calc_pi(500), math.pi))


################ Numpy ###############
import numpy as np
################  ###############

################  ###############

################  ###############


