"""
Created on Sun Feb 15 00:55:14 2015

@author: Enes Kemal Ergin

The Function: The Function and other preliminaries (Video 1)
"""

# Python Set Comprehension:
## Set defined 
s = {-4,4,-3,3,-2,2,-1,1,0}
## Takes only positive numbers from the set.
{x for x in s if x >= 0}
## {0,1,2,3,4}

""" 
We will often use a dictionary to represent a function with a 
    finite domain
"""

# Uniform Distributions:
## Rolling a dice
## possible outcomes 1,2,3,4,5,and 6
## Probabilities are 1/6 for each outcome.
## This is the dictionary version in python
pr = {1:1/6, 2:1/6, 3:1/6, 4:1/6, 5:1/6, 6:1/6}

## Flipping two coins
pr_coin = {('H', 'H'):1/4, ('H', 'T'):1/4, ('T', 'H'):1/4, ('T', 'T'):1/4,}