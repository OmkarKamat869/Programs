# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 23:35:22 2021

@author: Omkar  Kamat
"""

# Program to add salt and also making iterations
# In this I used While loop for iteration

import hashlib


word=input("Enter the word You want to encode = ")
salt =input("Enter the word you want to use as a salt = ")
iterations=int(input("Enter the number of times you want to iterate the hash = "))
enc=word.encode("utf-8")
salt=salt.encode("utf-8")

i=1
digest = hashlib.md5(enc.strip() + salt.strip()).hexdigest()
while i<= iterations-1:
  digest=digest.encode("utf=-8")
  digest = hashlib.md5(digest.strip()).hexdigest()
  i+=1

print(digest)





