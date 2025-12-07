import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
f = 0
i = 0
while True:
    if i == 0:
        u=input("Give constant value ('-' to stop)")
    else:
        u=input(f"Give coefficient of the {i}th degree x ('-' to stop)")
    if u =='-':
        break
    else:
        try:
            u=float(u)
            f+=u*(x**i)
            i+=1
        except ValueError:
            print('Error! coefficient must be a constant!!')
print(f"f(x)={f}")
w = input('What do you want to do?? \n 1. Derive (d/dx) \n 2. Calculate limit \n 3. Find roots \n 4.  Factor \n 5. Apply the Bolzano Theorem \n 6. Apply the Rolle Theorem \n >>>  ')
if w == '1':
    print(f"The derivative f'(x)={sp.diff(f,x)}")
elif w == '2':
    lim = 0
    while True:
        appr = input('Give the value that you want the x to approach. (+inf for infinity, -inf for -infinity)')
        if appr == 'inf':
            lim = sp.limit(f,x,sp.oo)
            break
        elif appr == '-inf':
            lim = sp.limit(f,x,-sp.oo)
            break
        else:
            try:
                appr = float(appr)
                lim = sp.limit(f,x,appr)
                break
            except ValueError:
                print('Error! Please plug a number, inf or -inf!!')


    print(f"Limit of f(x) as x approaches {appr}, is {lim}")

elif w == '3':
    print(sp.real_roots(f)) 
elif w == '4':
    print(sp.factor(f))
elif w == '5':
    while True:
        while True:
            x1 = input('Give value 1 of closed interval \n >>> ')
            try:
                x1 = float(x1)
                break
            except ValueError:
                print('Error!! Please input a number!')
        while True:
            x2 = input('Give value 2 of closed interval \n >>> ')
            try:
                x2 = float(x2)
                break
            except ValueError:
                print('Error! Try putting in a number!')
        if x1 <= x2:
            break
        else:
            print('Error! Value 1 must be smaller than Value 2 ')
        
    print(f"The selected interval: [{x1},{x2}]")
    
    f1 = f.subs(x,x1)
    f2 = f.subs(x,x2)

    if f1*f2<0:
        print(f"Based on the Bolzano Theorem, there exist atleast one root in ({x1},x{x2}) of f(x)")
    elif f1*f2 == 0:
        if f1 == 0:
            print(f"Root: {x1}")
        else:
            print(f"Root: {x2}")
    else:
        print(f"There are not real roots of f(x) in ({x1},{x2})")
elif w == '6':
    print(f"The derivative of f(x)={sp.diff(f,x)}")
    while True:
        while True:
            x1 = input('Enter value 1 of closed interval \n >>> ')
            try:
                x1 = float(x1)
                break
            except ValueError:
                print('Error! value must be a number')    
            
        while True:
            x2 = input('Enter value 2 of closed interval')
            try:
                x2 = float(x2)
                break
            except ValueError:
                print('Error! Value must be a number')
        if x1<=x2:
            break
        else:
            print('Error! Value 1 must be equal or less than Value 2!! ')
    print(f"The selected interval: [{x1},{x2}]")
    print(f"The derivative of f: {sp.diff(f,x)}")
    f1 = f.subs(x,x1)
    f2 = f.subs(x,x2)

    if f1 == f2:
        print(f"Based on the Rolle Theorem, there exists at least one real root of f'(x) in ({x1},{x2})")
    else:
        print(f"The theorem does not apply!")



else:
    print('Error!')