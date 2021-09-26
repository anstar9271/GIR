# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 12:14:54 2021

@author: Dell
"""


import grule as a
import leveas as b
import levmed as c
import levhard as d

a.welcome()
a.rule()
print("'1' for Easy")
print("'2' for Medium")
print("'3' for Hard")
plyinp=int(input("Which level do you want to choose? :"))

if plyinp==1:
    b.easy()
    b.scoreread()
    
elif plyinp==2:
    c.medm()
    c.scoreread()
    
    
elif plyinp==3:
    d.hard()
    d.scoreread()
    
else:
    print("Invalid Input!!!")
    
    
op=input("New Game? (Y/N):")
while op=="Y" or op=="y":
    plyinp=int(input("Which level do you want to choose? :"))

    if plyinp==1:
        b.easy()
        b.scoreread()
        
    elif plyinp==2:
        c.medm()
        c.scoreread()
        
    elif plyinp==3:
        d.hard()
        d.scoreread()
        
    else:
        print("Invalid Input!!!")
        
    op=input("New Game? (Y/N):")