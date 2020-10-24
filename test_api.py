# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:13:10 2020

@author: dwolf
"""

import pytest
import requests
import json


def test_valid_login():
    url = "https://reqres.in/api/login"
    #data = {'email': 'abc@xyz.com', 'password': 'querty'}
    data = {'email': "eve.holt@reqres.in", 'password': "cityslicka"}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    print("Response text:" + response.text)
    print("Token is: ", token)
    print("Token type is: ", type(token))
    if "token" in token:
        print("Found token in token")
        assert token["token"] == "QpwL5tke4Pnpja7X4"
    else:
        print("Found token not in token")
    
def test_invalid_user_login():
    url = "https://reqres.in/api/login/"
    data = {'email': 'abc@xyz.com', 'password': 'querty'}
    #data = {'email': "eve.holt@reqres.in", 'password': "cityslicka"}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 400
    print("Response text:" + response.text)
    print("Token is: ", token)
    print("Token type is: ", type(token))
    if "token" in token:
        print("Found token in token")
        assert token["token"] == "QpwL5tke4Pnpja7X4"
    else:
        print("Found token not in token")
    
def test_missing_password_login():
    url = "https://reqres.in/api/login/"
    #data = {'email': 'abc@xyz.com', 'password': 'querty'}
    data = {'email': "eve.holt@reqres.in"}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 400
    print("Response text:" + response.text)
    print("Token is: ", token)
    print("Token type is: ", type(token))
    if "token" in token:
        print("Found token in token")
        assert token["token"] == "QpwL5tke4Pnpja7X4"
    else:
        print("Found token not in token")
        
def test_list_users():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    user = json.loads(response.text)
    print("Response Status code =", response.status_code)
    print("Response test = ", response.text)
    print("users type is: ", type(user), " number of entries is: ", len(user))
    data = user["data"]
    print("data type is: ", type(data), " number of entries is: ", len(data))
    ad = user["ad"]
    print("data['email'] =", data["email"])
    return user
    
def list_dict(data):
    if type(data) is dict:
        for key,value in data.items():
            if type(value) is dict:
                print("Key :", key)
                list_dict(value)
            else:
                print("Key/value =:", key, " : ", value)
        
list_dict(test_list_users())
#test_valid_login()