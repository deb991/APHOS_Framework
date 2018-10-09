#!/usr/bin/env python
import os
import sys
from threading import Thread
import ctypes
from subprocess import *
from datetime import datetime

drives = []
dict = {}

class serv():
    def __init__(self):
        print('~~~~  ::Initiating service for File server on Native System::  ~~~~\n')

    

    def file__Manager(self):
        parent_dir = ('/')
        print('\n Root filesystem syntex depends upon Platforms. ~~~~')
        print('\nWindows File system starts with \n<<C as Primary Parent Drive>>\n <<"/" as Primary Parent Drive/ Directory Location for both Unix, Mac>>')
        try:
            print('Parent Directory:: ~~~~\n')
            os.system(START "C:\\Users")

        except:
            print('Parent Directory:: ~~~~\n')
            os.system('START "/"')

if __name__ == '__main__':
    inst = serv()
    inst.file__Manager()
