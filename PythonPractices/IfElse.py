#!/usr/bin/python
#Given an integer,perform the following conditional actions:
"""
If is odd, print Weird
If
is even and in the inclusive range of to
, print Not Weird
If
is even and in the inclusive range of to
, print Weird
If
is even and greater than , print Not Weird
"""
#if __name__ == '__main__':
N = int(input())
if((N%2==1) or (N>5 and N<21)):
	print("Weird")
else:
        print("Not Weird")
