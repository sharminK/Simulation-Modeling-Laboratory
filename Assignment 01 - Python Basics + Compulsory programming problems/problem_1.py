# -*- coding: utf-8 -*-
"""Problem-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M6Z4jC2LHCrvYyiBM1o4-FgxJFVNOqIx
"""

x = int(input("Input any number: "))

# first half
for first in reversed(range(0,x)):

    for space in range(0,first):
        print(" ", end="")   

    for star in reversed(range(first,x)):
        print("*", end="")

    print("")        

# second half   
for second in reversed(range(0,x-1)):
      
    for space in reversed(range(second,x-1)):
        print(" ",end="")
        
    for star in range(0,second+1):
        print("*", end="")

    print("")