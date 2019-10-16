# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:21:46 2019

@author: ccc32
"""
import math
def prime_number(num):
    if num <= 3 and num > 0:
        return True
    sqrt_num = round(math.sqrt(num))
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            return False

    return True


# when this number is large
import math, random
def prime_number(num):
    if num <= 3 and num > 0:
        return True
    test1 = random.randint(2,num)
    test2 = random.randint(2,num)
    test3 = random.randint(2,num)
    if test1**num % num != test1:
        return False
    if test2**num % num != test2:
        return False
    if test3**num % num != test3:
        return False

    return True


# 经典的bayesian，一个疾病发病率0.1%，一个diagnostic test 有1% misclassification，
# 问如果test阳性，实际患病的概率。这道题值得注意的是missclassification
# 包括false positi‍‌‌‍‍‍‍‍‍‍‌‍‌‌‍‌ves和false negatives。

# P(disease|+) = P(disease, +) /P(+) = .1% * 99%/(.1%*99% + 99.9%*1%)
    

#The Fibonacci numbers, commonly denoted F(n) form a sequence, 
# called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

#F(0) = 0,   F(1) = 1
#F(N) = F(N - 1) + F(N - 2), for N > 1.
#Given N, calculate F(N).
 def fibonacci(n):
    if n<2:
        return n
    fib=[0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib[n]


    
def fibonacci(n):
    if n<2:
        return n
    fn2=0
    fn1=1
    for i in range(2,n+1):
        fn = fn2 + fn1
        fn2= fn1
        fn1 = fn
        
    return fn


#recursive solution
def fibonacci(n):
    if n < 2:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)


# leetcode 77
    #Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
def combine(n: int, k: int):
        result = []
        if k == 0:
            return result
        if k == 1:
            for i in range(1,n+1):
                result.append([i])
            return result
        
        if k >= 2:
            result_k1 = combine(n, k-1)
            for i in range(len(result_k1)):
                k1_i = set(result_k1[i])
                for j in range(n):
                    if j+1 in k1_i:
                        continue
                    elif j+1 > result_k1[i][-1]:
                        k_ij = result_k1[i] + [j+1]
                        result.append(k_ij)
            return result
        
        
#sampling
# 给两个数组，第一个是要sample的对象，这里的例子是['a', 'b', 'c']
# 第二个数组是概率，比如[0.3, 0.4, 0.3]. 相加等于1
# 写一个函数，每次输出一个sample的对象，概率要符合给出的概率
import random
def sampling(l:list, w:list):
    rand = random.uniform(0,1)
    
    w_cul = [w[0]]
    for i in range(1, len(w)):
        w_cul.append(wcul[i-1] + w[i])
    for j,w_c in enumerate(w_cul):
        if rand < w_c:
            return j
    return len(w)-1


def sampling(l:list, w:list):
    rand = random.uniform(0,1)
    
    w_cul = [w[0]]
    for i in range(1, len(w)):
        w_cul.append(w_cul[i-1] + w[i])
    left = 0
    right = len(w) - 1
    while left + 1 < right: # prevent infinite loop
        mid = (left + right) // 2
        if rand > w_cul[mid]:
            left = mid
        else:
            right = mid
    if rand < w_cul[left]:
        return left
    else:
        return right


    
# Question 1.  将string倒写， 比如 “hello word!" 写成 "!drow olleh"
def reverse_string(string):
    result = ''
    for i in range(1, len(string)+1):
        result += string[-i] 
    return result
 
def reverse_string(string):
    result = ''
    for i in range(len(string)-1, -1, -1):
        result += string[i]
    return result
       

def reverse_string(string):
    return string[::-1]
        
#Question 2. 写一个function，input是string， output要数字母和字母个数。比如 input：“BBWWWB”; output：“2B3W1B”
def count_letter(string):
    if len(string) < 1:
        return ''
    counter = 1
    result = ''
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            counter += 1   
        else:
            result += str(counter) + string[i-1]
            counter = 1
    result += str(counter) + string[-1]

    return result

def countChar(string):
    counter = 0
    output = ''
    prev = ''
    for char in string:
        if char != prev:
            counter = 1
            output +=str(counter) + char
        else: # when current char == prev
            counter+=1
            output = output[:-2]
            output +=str(counter) + char
         
        prev = char
    return output



def numfind(word):
    prev = None
    output = ""
    for letter in word:
        if letter != prev:
            output += "1" + letter
        else:
            output = output[:-2] + str(int(output[-2])+1) + output[-1]
        prev = letter
    return output
            

#leetcode 387
#  Given a string, find the first non-repeating character in it and 
# return it's index. If it doesn't exist, return -1. 
    
def uniq_char(string):
    for i, char in enumerate(string):
        count_char = string.count(char)
        if count_char == 1:
            return i    
    return -1


def firstUniqChar(s):
        letters = {}
        for c in s:
            letters[c] = letters[c] + 1 if c in letters else 1
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1
    
#leetcode 139
        
    
    
#Given a list of strings: ['running, 0800, 1000', 'swimming,1000,1100', 
# 'eating,1100,1200','running,1115,1330'...]. The meaning of the strings are 'activity, start time, end time'
#prob1. Write a function to output all the unique activities in the list
#prob2. Write a function to calculate the duration of each activity in minutes
#prob3. Write a function to merge all the time intervals in the list that have 
#    overlaps, leave the non-overlapping intervals alone, and finally output 
#    all non-overlapping time intervals after merging those that overlap. O(N^2) solution not acceptable.

input_strings = ['running, 0800, 1000', 'swimming,1000,1100', 'eating,1100,1200','running,1115,1330']
def uniq_act(strings):
    acts = []
    for s in strings:
        act = s.split(',')[0]
        acts.append(act)
        
    return set(acts)

def duration(strings):
    times = []
    for s in strings:
        s_list = s.split(',')
        after = s_list[2]
        before = s_list[1]
        time = (int(after[:-2])- int(before[:-2])) * 60 + int(after[-2:])  - int(before[-2:])
        times.append(time)
    return times

def remove_overlap(strings):
    i = 1
    while i < len(strings):
        string1 = strings[i-1].split(',')
        string2 = strings[i].split(',')
        start1 = string1[1]
        start2 = string2[1]
        end1 = string1[2]
        end2 = string2[2]
        if start2 < end1:
            strings[i-1] = string1[0] + ' and ' + string2[0] + ',' + start1 + ',' + str(max(int(end1), int(end2)))
            strings.remove(strings[i])
        else:
            i += 1
    return strings
            