# -*- coding: utf-8 -*-
"""Problem-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M6Z4jC2LHCrvYyiBM1o4-FgxJFVNOqIx
"""

x = int(input("Input any number: "))

# first half
for first in range(0,x):

    for space in range(first,x-1):
        print(" ", end="")   
        
    print("*", end="")

    for space in range(0, (first*2)-1):
        print(" ", end="")

    if first==0:
        print("") 
     
    else:
        print("*")
      

#print("")
#second half
for second in reversed(range(0,x-1)):

    for space in range(second,x-1):
        print(" ", end="")   
        
    print("*", end="")

    for space in range(0, (second*2)-1):
        print(" ", end="")

    if second==0:
        print("") 
     
    else:
        print("*")