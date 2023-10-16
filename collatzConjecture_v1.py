# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:56:29 2023

@author: eirankunda
"""

import matplotlib.pyplot as plt
import numpy as np
import time

#filt the inputs. Allow only numbers!
hand = True
while hand == True:
    try:
        n = int(input('Enter an integer to begin the sequence: '))
        hand = False 
    except:
        print('Unsupported Input. Try again...')
        
#keep my values
colSequence = []
while n!= 1:
    colSequence.append(n) #the first value will be added to the sequence
    if n%2 == 0:
        n = n //2 
    else:
        n = 3*n + 1
colSequence.append(n) #the list is updated each time the program update the value of n
        
print(f'The collatz Sequence is:\n {colSequence}')
print(f'The peak for the sequence appeared at {max(colSequence)}')
print(f'The least number for the sequence appeared at {min(colSequence)}')


plt.figure(facecolor = 'yellow')
plt.axes().set_facecolor(color = 'pink')

plt.plot([i for i in range(len(colSequence))],colSequence, color='blue')
plt.title('Collatz conjecture')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.show()
