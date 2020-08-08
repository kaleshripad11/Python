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

"""
Output
$ python3 keywords.py 
False
None
True
and
as
assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield

"""
