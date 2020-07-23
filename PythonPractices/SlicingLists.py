'''
Created on 07-Jun-2020

@author: shree
'''
lists = [1,2,4,5,[9,34,23,"python"],6,0,7,8,2,'a',78,True]  

print(len(lists))

print(lists[2:7])   #O/P : [4, 5, 6, 7, 8]

print(lists[::-1])
print(lists[:-1])

print(lists[-2::-7])

print(lists[4][3])