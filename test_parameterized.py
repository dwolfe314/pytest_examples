# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:08:06 2020

@author: dwolf
"""
import pytest
@pytest.mark.parametrize("x,y,z",[(10,20,200),(20,40,200)])

def test_method(x,y,z):
    assert x*y == z