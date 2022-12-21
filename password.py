#!/usr/bin/python3
# -*- coding: ascii -*-

import random as rd
import time
import math

#Date of Creation: Dec 21st 2022
__author__ = "Sizusyantra"
__version__ = "1.0"
__maintainer__ = "Sizusyantra"

class password:
    'Class password is a string object that generates a pseudo random password based on digits, letters and simbols'
    def __init__(self,length):
        'This is a constructor function for class defines the elements of the password'
        self.length = length
        self.digits = "1234567890"
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.simbols = "!@#$*()_-=+/?><."
    
    def generate (self):
        'Generating function of the password'
        password = ""
        for i in range(self.length):
            number = rd.randint(1,3)
            if number == 1:
                password = password + self.digits[rd.randint(1,9)]
            elif number ==2:
                password = password + self.letters[rd.randint(1,25)]
            else: 
                password = password + self.simbols[rd.randint(1,10)]
        return password



def __main__():
    MyPassword = password(10)
    print(MyPassword.__doc__)
    print("Your password is:"+MyPassword.generate())

if __name__ == '__main__':
    __main__()
