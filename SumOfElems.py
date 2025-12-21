# -- encoding:utf-8 --

import array
import os
import random

os.system("cls")
print("Input a count of elements")
nElems = int(input())
iArray = array.array("i")
nSum = 0
for i in range(0, nElems - 1):
    nItem = random.randint(1, 50)
    iArray.append(nItem)
print("Generated Array:")
for i in range(0, nElems - 1):
    nSum += iArray[i]
    print(iArray[i], end=" ")
print(f"\r\nThe Sum of {nElems} elements of the array is:{nSum}")