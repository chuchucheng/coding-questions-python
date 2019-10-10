name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# 制表符\t
# 换行符\n

name.rstrip()  #right
name.lstrip()  #left
name.strip()   #both

3 ** 3

str(23)

###################list and tuple ################
names = ["peter",'mary','jack']
names.append('lisa')
names.insert(0,'ella')
del names[0]


popped_names = names.pop()
print(names)
print(popped_names)
names.pop(0)


nocome = 'jack'
names.remove(nocome)
print(names)
print("\n" + nocome.title() + " is not coming.")

names.sort() # permanant sorting
names.sort(reverse=True)


places = ['paris', 'praha', 'zurich', 'amsterdam', 'london', 'beijing', 'budapest', 'madrid', 'berlin', 'moscow', 'new york', 'boston', 'san franscisco']


print(sorted(places)) # temporary sorting
print(sorted(places, reverse = True))

names.reverse()  #reverse original order

print('I am goint to ' + str(len(places)) + ' places.')

for place in places:
    print('I love ' + place.title() + '.')
print('I wish I could go to all of them.')

three_numbers = list(range(3,31,3))
print(three_numbers)

cubes = [value**3 for value in range(1,11)]
print(cubes)

print('My favorate places are:' )
print(places[-3:])

#copy should using slicing, otherwise change will transfer
friend_places = places[:]
places.append('san jose')
friend_places.append('tokyo')
for place in places:
    print(place)
    

##tuple unchangeble
dimensions = (200,100)
dimensions = (400,100)

############# if ###################
if 'paris' in places and 'london' not in places:
    print('It is in the list!')
elif 'beijing' in places:
    print('yay!')
else:
    print('Look for other places!')


##check if list is empty
requested_toppings = []
if requested_toppings:  ### this checks empty list
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")
    
    
fav_places = ['prague', 'beijing','jincheng', 'newton']

for place in fav_places:
    if place.lower() in places:
        print(place +' match!')
    else:
        print(place + ' not matched!')


###############dictionary ##################
        
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

del alien_0['speed']

for k, v in alien_0.items():
    print(k + ': ' + v)

for k in alien_0.keys():
    print(k.title())

for k in alien_0:
    print(k)
    
for key in sorted(alien_0.keys()):
    print(key)
    
for value in set(alien_0.values()):
    print(value)
# set similar to list, but only unique values
    
users = {
        'aeinstein': {
                'first': 'albert',
                'last': 'einstein',
                'location': 'princeton',},
        'mcurie': {
                'first': 'marie',
                'last': 'curie',
                'location': 'paris',},
         }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

#############################input and while###############
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
    

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)  

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)
        

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  #back to top
    print(current_number)


# for can't modify list, but while can

### move between lists
unconfirmed_users = ['alice','brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
print("\nThe following users have benn confirmed:")
for user in confirmed_users:
    print(user.title())

### delete certain elements
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)


### text
message = "I really like dogs."
message.replace('dog', 'cat')
message.count('dogs')
message.lower().count('dogs')

###fill dictionary
responses = {}
polling_active = True

while polling_active:
    name = input('\nPlease type your name:')
    response = input('Which moutain?')
    
    responses[name] = response
    
    repeat = input("Would you liked to invite another person? yes/no ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')
    

########################### function ###################
def greet_user():
    print('Hi!')
    
greet_user()


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name +  ' ' + last_name
    return full_name.title()

print(get_formatted_name('jimi', 'hendrix'))
print(get_formatted_name('john', 'hooker', 'lee'))
        

#each function for one job

### multiple input
def make_pizza(size, *toppings):
    """possible multiple toppings"""
    print('\nMake a ' + str(size) +
          '-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)
        
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


### multiple inputs with keywords
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

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

import os
path = 'C:\\Users\\ccc32\\Box Sync\\github\\coding-questions-python'
os.chdir(path)

#import self-built module
import build_profile as bp
# from module import function
user_profile = bp.build_profile('Ella', 'Green', age=23, location='SF')
# no spaces near '=' for parameters


#standard packages
# ordered dictionary, based on input order
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'


from random import randint
x = randint(1,6)

    
################# read and write files ########################
# with closes file appropriately
filename = 'pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

#### write 
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
# if file did not exist, will create one
    
### attach to existing file, not re-write
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")



################ debug  ##############
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
        

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # pass
        # if simply pass, nothing will be done
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split() #split into words
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
        
        
################# json #####################
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
    
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    
    
    
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()



####################### debug ###############################
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

# method must start with test!

'''
    assertEqual(a, b) 
    assertNotEqual(a, b) 
    assertTrue(x) 
    assertFalse(x) 
    assertIn(item, list) 
    assertNotIn(item, list)
'''


## debug class
class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in responses:
            print('- ' + response)


import unittest
class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()