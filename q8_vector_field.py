import numpy as np
import numpy.linalg as la


def f(x,a=1,b=2,c=3):
    return a * x**2 + b * x + c

def cdiff(f,X,h):
  return (f(X + h) - f(X - h)) / (2 * h)
  
  
def v(x,y):
  return (2*x*y,x**2*y**2)
# Euler's method step
def euler(x=4, y=2, h=.5, v=v,n=2):
  for _ in range(n):
    vx, vy = v(x, y)
    x = x + h * vx
    y = y + h * vy 
  return x, y

  
# Compute the 5th point in the (2, 3) Halton sequence
# x = halton_sequence(5, 2)
# y = halton_sequence(5, 3)
def halton_sequence(index, base):
  result = 0
  f = 1 / base
  i = index
  while i > 0:
      result += f * (i % base)
      i = i // base
      f = f / base
  return result