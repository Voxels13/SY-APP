#Creating a one dimensional NumPy array containing numbers between 1 - 10

import numpy as np

arr = np.arange(1,11)

print(arr)
print()

#Creating a one dimensional NumPy array containing numbers between 1 - 10

import numpy as np

arr = np.arange(1,11)

print(arr)
print()

#array

arr1 = np.array([4,2,1,3,7,9])

print(arr1)
print()

#arange with step value

arr2 = np.arange(0,11,2)

print(arr2)
print()

#Sorting numpy arrays

arr3 = np.sort(arr1)

print(arr3)
print()

#Functions on array's

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a*b)    #element-wise product
print(a@b)    #Matrix product v1
print(a.dot(b)) #Matrix product v2
print(a+b)  #Adds element-wise
print(a-b) #subtracts element-wise
print()

#Concatenation of two numpy arrays

print(np.concatenate((a,b)))

#numpy aggregate functions

#sum --> np.sum()
#mean --> np.mean()
#median --> np.median()
#standard deviation --> np.std()

print()

#Assignment 1

#A fitness band records a user's heart rate every minute for 10 minutes during exercise

from numpy import random

bpm = np.random.randint(80,151,10)

print(f"Heart rates:{bpm}\n")

ff = bpm[:5]
sf = bpm[5:]

print(f"BPM of first 5 minutes:\n{ff}\n")

print(f"Max:{max(bpm)}")
print(f"Min:{min(bpm)}")
print(f"Avg:{np.mean(bpm)}\n")

temp = bpm > 120

print(f"Heart rates above 120 BPM:{bpm[temp]}")
print(f"Heart rates with minutes (1-indexed): {np.where(temp)[0]+ 1}")


