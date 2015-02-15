"""
Created on Sun Feb 15 02:03:41 2015

@author: Enes Kemal Ergin

The Field: Playing with C (Video 3)
"""

## Gets a list of complex numbers
l = [2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j]
## Calling plotting module from plot library
from plotting import plot # This module is provided by the Course.
## Puts every point in the list l into the complex space.
plot(l)

## Takes the absolute, distance to the origin of the complex
abs(1+1j)
# 1.4142135623730951

## Scaling by 0.5
plot({0.5 * z for z in l})

## Reflection (multiplying by -)
plot({(-1) * z for z in l})

## Rotating by 90 degrees (multiplying by i)
