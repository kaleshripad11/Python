'''
Created on 18-Jun-2020

@author: shree
'''
import sys as s
import GetKeyWordList as l
print(s.api_version)
print(s.getprofile())
print(s.__package__)
print(s.__name__)
print(s.platform)
print(l.__name__)

if __name__ == "__main__":
    print(True)
    
else:
    print(False)