#!/usr/bin/python

import os
op = input('Do you want to shutdown your system(Yes/No)?\n')
if(op=='Yes' or op == 'y'):
    os.system('shutdown now')
else:
    print('Shutdown aborted')
