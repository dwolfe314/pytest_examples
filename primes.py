# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:06:16 2020

@author: dwolf
"""

def is_prime(number):
    # Return True if number is prime
    if number == 1: # one is not prime but will return True below
        return False
    for element in range(2,number):
        if number % element == 0:
            return False
        return True
    