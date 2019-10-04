spam = "dog"
len(spam)

#string methods
spam.capitalize()
spam.endswith("og")


#str, int, float
my_num = input("Input a number:")
my_num = float(my_num)
print(my_num)



temp = input('input temp in C:')
temp = float(temp)
if temp< -273.15:
    print('impossible')
else:
    temp = 9/5*temp + 32
    print(temp)


#count spaces
sentence = input('sentence:')
sentence = sentence.strip()
while '  ' in sentence:
    sentence = sentence.replace('  ',' ')
n_spaces = sentence.count(' ')
print('n of spaces is ' + str(n_spaces))



##boolean comparison
type(True)
#and, or, not
if 5>0:
    print('pos')
elif 5<0:
    print('neg')
else:
    print('zero')



spam = 5
if type(spam)==int or type(spam)==float:
    if spam>0:
        print('pos')


from random import choice
computer_choice = choice(['r','p','s'])

your_choice = ' '
while your_choice != 'r' and your_choice != 's' and your_choice != 'p':
    your_choice = input('your choice is: ')

if your_choice == computer_choice:
    print('tie')
elif your_choice == 'r':
    if computer_choice == 's':
        print('win')
    elif computer_choice == 'p':
        print('lose')
elif your_choice == 's':
    if computer_choice == 'p':
        print('win')
    elif computer_choice == 'r':
        print('lose')
elif your_choice == 'p':
    if computer_choice == 'r':
        print('win')
    elif computer_choice == 's':
        print('lose')
else:
    print('invalid')


while spam <3:
    print(spam)
    spam = spam +1
    if spam >3:
        break

for i in range(2,10,2):
    print(i)



import math
math.log(5)

from math import log, factorial
log(5,9)
factorial(4)

def factorial(x):
    f = 1
    for i in range(1,x+1):
        f = f*i
    return f

def print_square(start, end):
    for i in range(start, end+1):
        print(i**2)

spam = [1,2,3]
pets = ['cat','dog','fish']
eggs = [[1, 'dog'],[2,'cat']]

pets[1] = 'hamsters'
pets[0:2]
pets[:2]
pets[0:]
pets[-1]
'cat'[1]


for i in range(len(pets)):
    print(pets[i])

for i in pets:
    print(i)

for i in 'cat':
    print(i)

len(eggs)
spam + eggs
'cat' in pets

#python lists methods
pets.index('cat')
pets.append('gerbils')
pets.insert(1,'gerbils')
pets.remove('gerbils')
pets.pop(-1)
pets.sort()
pets.count('cat')


def prop_larger(l,n):
    j=0
    for i in l:
        if i>n:
            j = j+1
    return j/len(l)

def prop_larger(l,n):
    j=0
    for i in l:
        j = j+int(i>n)
    return j/len(l)



def get_squares(start, end):
    j = []
    for i in range(start, end+1):
        j.append(i**2)
    return j


#tuple unchangeble
spam = (1,2,3)

spam = [1,3,5]
[x**2 for x in spam]
[x**2 for x in range(1,4)]
[x for x in spam if type(x) == int and x>3]

import statistics
print(statistics.mean(spam))
sum(spam)

sum([x>3 for x in spam])/len(spam)
len([x>3 for x in spam])/len(spam)


##dictionary
my_name = {'first':'Chuchu', 'last':'C'}
my_name['last']


#  \nI back slash; \tI tab
add = r'C:\teaching'

#read in text file
f_in = open(r'C:\Users\ccc32\Desktop\a.txt')
#text = f_in.read()
lines = f_in.readlines()
f_in.close()

text = lines[0]
text.strip('\n')
lines = [x.strip('\n') for x in lines]

import os
print(os.path.join('C:', 'Users','ccc32'))
os.sep
os.getcwd()
os.chdir(r'path')
os.path.basename(r'C:\Users\ccc32\Desktop\a.txt')
os.path.dirname
os.listdir
[x for x in os.listdir(r'') if x.endswith('.txt')]


with open(r'') as f_in:
    text = f_in.read()


with open(r'C:\Users\ccc32\Downloads\S1_RTs.txt') as f_in:
    data = f_in.readlines()

data = [float(x.strip('\n')) for x in data]
statistics.mean(data)


#count spaces
def count_words(sentence):
    sentence = sentence.strip()
    while '  ' in sentence:
        sentence = sentence.replace('  ',' ')
    n = sentence.count(' ') + 1
    return n

#get the length of each sentence
with open(r'C:\Users\ccc32\Downloads\sentences.txt') as f_in:
    sentences = f_in.readlines()

sentences = [str(x.strip('\n')) for x in sentences]

n_words = [count_words(x) for x in sentences]
statistics.mean(n_words)


###scipy package
from scipy.stats import norm, ttest_rel, ttest_ind
norm.cdf(-1.96)

import numpy as np
from scipy.stats import t

norm.ppf(.925)

###simulation

n_simulations = 10000
N = 20
effect_size = 0.5

p_rel = np.full(n_simulations, np.nan)
p_ind = np.full(n_simulations, np.nan)


for i in range(n_simulations):
    #generate random data with some characteristics:
    X = norm.rvs(size = N, loc = 0)
    Y = norm.rvs(size = N, loc = effect_size)
    #loc = mean

    #calculations and save:
    p_rel[i] = ttest_rel(X,Y).pvalue
    p_ind[i] = ttest_ind(X,Y).pvalue

#Do sth with those results:
np.mean(p_rel<0.05)
np.mean(p_ind<0.05)

import pandas as pd

mem_data = pd.read_excel(r'C:\Users\ccc32\Downloads\mem_data.xlsx', index_col = 0)
flight_data = pd.read_csv(r'C:\Users\ccc32\Downloads\flights.csv')


mem_data['group']
mem_data.iloc[:,1]
mem_data.loc['S7':'S10','NEU_recog']

mem_data.loc['S10','NEG_recog']
mem_data.iloc[9,2]
np.mean(mem_data)
mem_data.mean()
mem_data.loc['S1':'S10'].mean()

mem_data.sort_values(by = ['NEU_recog', 'NEG_recog'], inplace = True)
mem_data.mean()['NEU_recog']

mem_data.describe()


mem_data.loc['S7', 'NEU_recog'] = 0.98
mem_data.loc[:, 'NEU_recog'] = np.nan
mem_data.loc[:, 'NEU_recog'] = np.arange(20)
mem_data.loc[:, 'new_col'] = np.nan

mem_data = mem_data.drop('new_col', axis=1)

flight_data.dropna(inplace = True)


def prop2perc(proportion):
    return proportion*100

mem_data[['NEU_recog', 'NEG_recog']] = mem_data[['NEU_recog', 'NEG_recog']].apply(prop2perc)


mem_data['diff'] = mem_data['NEG_recog']- mem_data['NEU_recog']
print(np.mean(mem_data.loc[:,'diff']))

mem_data[['NEU_recog', 'NEG_recog']] = mem_data[['NEU_recog', 'NEG_recog']].apply(np.log)

mem_data.iloc[:,1:3] = mem_data.iloc[:,1:3].apply(np.log)

mem_data.loc[mem_data['group'] == 'YA',:].mean()
mem_data.groupby('group').mean()['NEU_recog']

mem_data.group
mem_data.groupby('group').NEU_recog.mean()
#can group by a list of vars



flight_data.groupby('origin').dep_delay.mean()
flight_data.groupby('origin').dep_delay.median()

flight_data.loc[flight_data['dest'] == 'BOS'].arr_delay.mean()
flight_data.loc[flight_data['dest'] == 'BOS'].arr_delay.median()


mem_data['NEU_recog'].hist()
mem_data['NEU_recog'].plot()

mem_data = pd.DataFrame(mem_data)

mem_data.to_excel(r'path')


sentences = pd.read_excel(r'C:\Users\ccc32\Downloads\sentences.xls', header = None)
sentences = pd.DataFrame(sentences)
sentences['lenth'] = sentences.iloc[:,0].apply(count_words)

sentences.to_excel(r'C:\Users\ccc32\Downloads\sentences.xlsx')


#debug
spam = 5
assert type(spam) == str

import pandas as pd
import numpy as np
import os

S1 = pd.read_excel(r'C:\Users\ccc32\Downloads\S1.xlsx')
S2 = pd.read_excel(r'C:\Users\ccc32\Downloads\S2.xlsx')
S3 = pd.read_excel(r'C:\Users\ccc32\Downloads\S3.xlsx')

os.chdir(r'C:\Users\ccc32\Downloads\pythonbc')

sub_files = [file for file in os.listdir() if file.endswith('.xlsx')]

all_subs = pd.DataFrame()

for sub_file in sub_files:
    sub_id = sub_file[:-5]
    sub_data = pd.read_excel(sub_file)
    sub_data['categorization.rt_raw'] = pd.to_numeric(sub_data['categorization.rt_raw'], errors = 'coerce')
    sub_mean = sub_data.groupby('condition').mean()['categorization.rt_raw']

    #calculate means and store in summary data frame
    all_subs.loc[sub_id, 'NEU'] = sub_mean['NEU']
    all_subs.loc[sub_id, 'NEG'] = sub_mean['NEG']


from scipy.stats import ttest_rel

ttest_rel(all_subs['NEU'],all_subs['NEG'])


#For each word in stim_words.txt, calculate the number of orthographic neighbors
#found in SUBTLEXusFreqAbove1.txt. (An orthographic neighbor is a word
#that is the
#same length and exactly one letter different.)

with open(r'C:\Users\ccc32\Downloads\stim_words.txt') as f_in:
    stim_words = f_in.readlines()

stim_words = [x.strip('\n') for x in stim_words]

with open(r'C:\Users\ccc32\Downloads\SUBTLEXusFreqAbove1.txt') as f_in:
    subtle = f_in.readlines()

subtle = [x.strip('\n') for x in subtle]

def o_neighbors(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        words=zip(word1,word2)
        incorrect=len([c for c,d in words if c!=d])
        if incorrect == 1:
            return True
        else:
            return False

n_o_neighbors = []

for i in stim_words:
    result = []
    for j in subtle:
        result.append(o_neighbors(i,j))
    i_neighbors = sum(result)
    n_o_neighbors.append(i_neighbors)


### conda - package manager
 
