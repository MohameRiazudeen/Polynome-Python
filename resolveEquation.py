import matplotlib.pyplot as plt
import numpy as np
from math import pow
from math import sqrt

"""
Let us try to resolve the equation ax²+bx+c
"""
a=2
b=-6
c=4

# the formula delta= "b² - 4ac"  to find the root of the equation
delta = pow(b,2) - 4*a*c

# the two roots are x1 and x2 : (-b - ±\/delta) / 2a
x1 = (-b - sqrt(delta))/(2*a)
x2 = (-b + sqrt(delta))/(2*a)

"""
Plotting the graph with mathplotlib library
"""
font={'family':'serif','color':'red','size':15}
font1={'family':'serif','color':'blue','size':10}

# array of x axis and define its limit
x =np.arange(x1-10,x2+10,1)

# array of y axis
y=[]

# get all the values to plot the function f(x) = ax²+bx+c

for i in x:

        y.append(a*pow(i,2) + b *i + c)

plt.plot(x,y,color="red")

plt.title(f"Polynome graph {a}x^2 + ({b})x + ({c})", fontdict=font)

plt.xlabel("x axis",fontdict=font1)
plt.ylabel("y axis",fontdict=font1)

plt.savefig(f"{a}x^2+({b})x+({c})3.jpg")

