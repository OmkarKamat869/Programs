# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:55:35 2021

@author: Omkar  Kamat
"""

import turtle             
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)