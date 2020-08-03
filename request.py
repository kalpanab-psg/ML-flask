# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:50:17 2020

@author: apccf
"""
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())