# -*- coding: utf-8 -*-
"""Problem-X.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M6Z4jC2LHCrvYyiBM1o4-FgxJFVNOqIx
"""

import matplotlib.pyplot as plt
import math


A_x = [0]              
A_y = [10] 

B_x = [40]              
B_y = [10]                           

C_x = [20]              
C_y = [0]               

O_x=[]
O_y=[]

X_x=[]
X_y=[]

s_A = 4
s_B = 2
s_C = 3


for t in range (0, 10+1):
  print("Time:",t)
  x=0
  y=0
  O_x.append(x)
  O_y.append(y)

  x=0
  y=-0
  X_x.append(x)
  X_y.append(y)


  # A moving ppositive
  dist_O_A = math.sqrt(( O_x[t] - A_x[t] )**2 + (O_y[t] - A_y[t])**2)

  # B moving negative
  dist_X_B = math.sqrt(( X_x[t] - B_x[t] )**2 + (X_y[t] - B_y[t])**2)

  # C chased A
  dist_A_C = math.sqrt(( A_x[t] - C_x[t] )**2 + (A_y[t] - C_y[t])**2)

  
  print("C and A:",dist_A_C,"A:(",(A_x[t],A_y[t]),")")


  cos_theta_O_A = ( O_x[t] - A_x[t] ) /dist_O_A
  sin_theta_O_A = ( O_y[t] - A_y[t] ) /dist_O_A

  A_new_x = A_x[t] + s_A * cos_theta_O_A
  A_new_y = A_y[t] + s_A * sin_theta_O_A

  A_x.append(A_new_x)
  A_y.append(A_new_y)

  cos_theta_X_B = ( X_x[t] - B_x[t] ) /dist_X_B
  sin_theta_X_B = ( X_y[t] - B_y[t] ) /dist_X_B

  B_new_x = B_x[t] + s_B * cos_theta_X_B
  B_new_y = B_y[t] + s_B * sin_theta_X_B

  B_x.append(B_new_x)
  B_y.append(B_new_y)

  
  cos_theta_A_C = ( A_x[t] - C_x[t] )/dist_A_C
  sin_theta_A_C = ( A_y[t] - C_y[t] ) /dist_A_C
            
  C_new_x = C_x[t] + s_C * cos_theta_A_C
  C_new_y = C_y[t] + s_C * sin_theta_A_C

  C_x.append(C_new_x)
  C_y.append(C_new_y)


for t in range (0, 10+1):
  print("Time:",t)
  x=0
  y=0
  O_x.append(x)
  O_y.append(y)

  x=0
  y=-0
  X_x.append(x)
  X_y.append(y)


  # A moving ppositive
  dist_O_A = math.sqrt(( O_x[t] - A_x[t] )**2 + (O_y[t] - A_y[t])**2)

  # B moving negative
  dist_X_B = math.sqrt(( X_x[t] - B_x[t] )**2 + (X_y[t] - B_y[t])**2)

  # # C chased A
  # dist_A_C = math.sqrt(( A_x[t] - C_x[t] )**2 + (A_y[t] - C_y[t])**2)

    # C chased B
  dist_B_C = math.sqrt(( B_x[t] - C_x[t] )**2 + (B_y[t] - C_y[t])**2)
  
  print("B and C:",dist_B_C,"A:(",(A_x[t],A_y[t]),")")



  cos_theta_O_A = ( O_x[t] - A_x[t] ) /dist_O_A
  sin_theta_O_A = ( O_y[t] - A_y[t] ) /dist_O_A

  A_new_x = A_x[t] + s_A * cos_theta_O_A
  A_new_y = A_y[t] + s_A * sin_theta_O_A

  A_x.append(A_new_x)
  A_y.append(A_new_y)

  cos_theta_X_B = ( X_x[t] - B_x[t] ) /dist_X_B
  sin_theta_X_B = ( X_y[t] - B_y[t] ) /dist_X_B

  B_new_x = B_x[t] + s_B * cos_theta_X_B
  B_new_y = B_y[t] + s_B * sin_theta_X_B

  B_x.append(B_new_x)
  B_y.append(B_new_y)

  
  # cos_theta_A_C = ( A_x[t] - C_x[t] )/dist_A_C
  # sin_theta_A_C = ( A_y[t] - C_y[t] ) /dist_A_C
            
  # C_new_x = C_x[t] + s_C * cos_theta_A_C
  # C_new_y = C_y[t] + s_C * sin_theta_A_C

  # C_x.append(C_new_x)
  # C_y.append(C_new_y)

  cos_theta_B_C = ( B_x[t] - C_x[t] )/dist_B_C
  sin_theta_B_C = ( B_y[t] - C_y[t] ) /dist_B_C
            
  C_new_x = C_x[t] + s_C * cos_theta_B_C
  C_new_y = C_y[t] + s_C * sin_theta_B_C

  C_x.append(C_new_x)
  C_y.append(C_new_y)


# plt.figure(figsize=(15,8))
plt.plot(A_x,A_y,c='red')
plt.scatter(A_x,A_y,c='red')
plt.plot(B_x,B_y,c="blue")
plt.scatter(B_x,B_y,c="blue")
plt.plot(C_x,C_y,c="green")
plt.scatter(C_x,C_y,c="green")
plt.plot(O_x,O_y,c="yellow")
plt.scatter(O_x,O_y,c="yellow")
plt.plot(X_x,X_y,c="pink")
plt.scatter(X_x,X_y,c="pink")











