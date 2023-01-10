# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 23:14:30 2021

@author: Omkar  Kamat
"""

# Project2 = Program to generate hashes of a string using 3 different hash algorithms
# In this project I used md5, sha256 and sha512 algorithms

import hashlib

word=input("Enter the word You want to encode = ")
enc=word.encode("utf-8")
digest=hashlib.md5(enc.strip()).hexdigest()


enc=digest.encode("utf-8")
digest1=hashlib.sha256(enc.strip()).hexdigest()


enc=digest1.encode("utf-8")
digest2=hashlib.sha512(enc.strip()).hexdigest()


print("1st Hash using md5 = ",digest)
print("\n2nd Hash using sha256 = ",digest1)
print("\nFinal hashing using sha512 = ",digest2)