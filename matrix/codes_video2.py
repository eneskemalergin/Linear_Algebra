"""
Created on Sun Feb 15 01:52:42 2015

@author: Enes Kemal Ergin

The Field: Introduction to Complex Numbers (Video 2)
"""

# complex number = (real part) + (imaginary part) * i

## Pyhton use j for doing complex
1j

1+3j

(1+3j) + (10+20j)

x = 1+3j
(x-1)**2
# (-9+0j) -> -9

x.real
# 1.0

x.imag
# 3.0

## Write a procedure solve(a,b,c) to solve ax + b = c

def solve(a,b,c):
    return (c-b)/a

solve(10, 5, 30)

# We can use the same procedure to calculate complex numbers as well.

solve(10+5j, 5, 20)
# (1.2-0.6j)
# Same procedure works for complex numbers.
