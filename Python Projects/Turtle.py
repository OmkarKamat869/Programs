# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:23:17 2021

@author: Omkar  Kamat
"""
import turtle
a=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
col=('white','red','orange','yellow','green','pink','cyan')
a.speed(0)
for i in range (200):
    a.forward(i*4)
    a.right(91)
    a.color(col[i%7])
for i in range (3):
    a.forward(i*4)
    a.right(91)    
for i in range (2):
    a.forward(i*4)
    a.right(91)