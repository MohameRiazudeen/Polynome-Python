from sympy import *
from math import pow
x = Symbol('x')

answer = solve(x**2 - 4*x+1, x)
print("Solution of equation is : ",answer)

derivative =diff(x**2 - 4*x+1, x)
solution = solve(derivative,x)
max = pow(solution[0],2) - 4*solution[0]+1

print ("The derivative of x**2 - 4*x+1 :",derivative,"\nSolution of the derivative :",solution,"\nExtremum of the function :",max)

