## To get the list of keywords in python there is 
## built in module called keywords which is need to be imported
import keyword as k

## The variable keylist is of type list
## The keylist variable will be storing every single keyword
## present inside the module called as keyword
keylist = k.kwlist

## A loop is required to iterate through the list and get every single keyboard on new line
for i in range(0,len(keylist)):
	print(keylist[i],end="\n")

