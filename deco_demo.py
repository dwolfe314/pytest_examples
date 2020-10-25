# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:56:10 2020

@author: dwolf
"""
"""
This is a test file
created in the my_new_feature branch
"""

def decorator_demo(func):
    def inner():
        print("Decorator Demo")
        return func()
    return inner
@decorator_demo
def plain_function():
    print("I need to be decorated")
    
plain_function()

plain_function = decorator_demo(plain_function)
plain_function()