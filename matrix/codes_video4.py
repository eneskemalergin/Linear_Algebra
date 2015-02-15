"""
Created on Sun Feb 15 04:21:34 2015

@author: Enes Kemal Ergin

The Field: Playing with GF (Video 4)
"""

## 
def encrypt(p, k):
    return p + k

from GF2 import one # Provided from the Course...
k = one
p = one

c = encrypt(p, k)



