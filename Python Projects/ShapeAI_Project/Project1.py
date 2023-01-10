# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 23:01:22 2021

@author: Omkar  Kamat
"""

# Project 1 = Program to generate md5 hash of the given data

import hashlib

word=input("Enter the word You want to encode = ")
enc=word.encode("utf-8")
digest=hashlib.md5(enc.strip()).hexdigest()
print(digest)