'''
Created on 07-Jun-2020

@author: shree
'''
my_list = [1,2,34,'shree',56.7]
listz = []
print(my_list)

#List Functions
my_list.append([21,43,55])
print(my_list)

print(my_list.count(2))

my_list.extend((0,2,5,6))
print(my_list)

my_list.insert(0, "hello python")
print(my_list)

my_list[6].sort(key=None, reverse=True)
print(my_list[6])

my_list.reverse()
print(my_list)

print(my_list.index('shree', 2, 10))

my_list.pop(4)
print(my_list)

my_list.remove(56.7)
print(my_list)

listz = my_list.copy()
print(listz)
print(len(listz))

my_list.clear()
print(my_list)