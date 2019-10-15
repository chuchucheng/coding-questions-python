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
def 