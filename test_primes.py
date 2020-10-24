# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:11:21 2020

@author: dwolf
"""

from primes import is_prime

def test_five_is_prime():
    assert is_prime(5) == True
    
def test_four_is_not_prime():
    assert is_prime(4) == False

def test_one_is_not_prime():
    assert is_prime(1) == False
    