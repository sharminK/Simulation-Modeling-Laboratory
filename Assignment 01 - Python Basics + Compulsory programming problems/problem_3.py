# -*- coding: utf-8 -*-
"""Problem-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M6Z4jC2LHCrvYyiBM1o4-FgxJFVNOqIx
"""

n = 1
n1, n2 = 0, 1
count = 0

if n <= 0:
   print("Please enter a positive num")
elif n == 1:
   print(n1)
else:
   print("Fibonacci num:")
   while count < n:
       print(n1)
       sum = n1 + n2
       # update values
       n1 = n2
       n2 = sum
       count += 1