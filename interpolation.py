import numpy as np
import numpy.linalg as la


def barycentricCoords():
  return  



def rbfInterpolation(x = np.array([.2,.8,.7]),fx = np.array([1.04,1.64,1.49]), kernel='inverseDistance', lam = 1):
  k = lambda a,_ : a
  A = []
  match kernel:
    case "inverseDistance":
      k = lambda r : 1/(1+r**2)
      A = createAfromSingleVarKernel(x,k)
    case "gaussian":
      k = lambda r,lam : np.exp(-lam*(r**2))
      A = createAfromTwoVarKernel(x,k,lam)
    case _:
      k = lambda r,_ : 1/(1+r**2)
  
  w = la.solve(A,fx)
  interpolationFunction = lambda point : np.sum (w*np.array([k(la.norm(point-xi)) for xi in x]))
  return A,w,interpolationFunction

def createAfromSingleVarKernel(x,k):
    n = len(x)
    A = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            r = la.norm(x[i]- x[j])
            A[i, j] = k(r)
    
    return A
  
  
def createAfromTwoVarKernel(x,k,lam):
    n = len(x)
    A = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            r = la.norm(x[i]- x[j])
            A[i, j] = k(r,lam)
    return A