import numpy as np
import numpy.linalg as la


# https://d3c33hcgiwev3.cloudfront.net/H1kf3a9JQnmZH92vSYJ52g_b5fd604170b54dbba960403f551d3284_519-7-1.pdf?Expires=1717891200&Signature=hfBQK97bMmkyozR74LrVYQULOppD3OZWvmvJH9ZwOQyb0oJtuDxx-HZ4MhsBVvUf08C~J5IBzVDorYHjtooCy69Mq6HaAJ7bmso0dAcR0EUcGEbHLkAZFnMffDZfSp61Xihk1eGrE1vSz-fqpg7A-6mUrbj7s12hQx33cuG9EvI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
# given two points, and their values, find the value of a midpoint
def linearInterpolation(x=np.array([[0,0],[10,0]]),fx=np.array([4,20]), p =np.array([7.5,0])):
  p0=x[0]
  p1=x[1]
  t = la.norm(p-p0)/la.norm(p1-p0)
  ft = (1-t)*fx[0]+t*fx[1]
  return ft

# given four points of a square, and their values, find the value of a point inbetween them
def bilinearInterpolation(x=np.array([[[1,0],[1,1]],[[2,0],[2,1]]]),
                          fx=np.array([[84,81],[91,61]]),
                          p =np.array([1.3,.8])):
  npx0=  np.array([x[0][0][0],p[1]]) # assume x vals are same
  f0 =linearInterpolation(x[0],fx[0],npx0)
  npx1=  np.array([x[1][0][0],p[1]]) # assume x vals are same
  f1 = linearInterpolation(x[1],fx[1],npx1)
  f3 =linearInterpolation(np.array([npx0,npx1]),np.array([f0,f1]), p)
  return f3

# https://d3c33hcgiwev3.cloudfront.net/fB9nVvgeRyKfZ1b4HlciNA_5d3cc1352340436ab89babe8f9baa74f_519-7-3.pdf?Expires=1717545600&Signature=LrmUo-8pbB-eqkO1yYzZdqsnnoiZSWnNSQpQ8PyGU5x7-QSgEU9rVNmFwOnTBdaO1edkSIj8DcI7bgpePUonM3qEZTcnKEWvKmjqjV8Ij3HjEyDQ~mDV~AqGV39bAuCrS7WSz9UwWhCk4wb8~KfXwjIG8zIkj7mKwEm9QB1XUEQ_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
# 2D or 3D only
def barycentricCoordsTriangle(triPoints = np.array([[0,-3],[0,3],[6,0]]),
                              ftripoints=np.array([[4,9,20],[24,0,18],[12,3,15]]),
                              p=np.array([2,2])):
  v1 = triPoints[0]
  v2 = triPoints[1]
  v3 = triPoints[2]
  e1 = v3-v2
  e2 = v1-v3
  e3 = v2-v1
     
  def computer(p):
    d1 = p-v1
    d2 = p-v2
    d3 = p-v3
  
    # Compute the cross product of e1 and e2
    cross_e1_e2 = np.cross(e1, e2)

    # Compute the norm of the cross product
    norm = np.linalg.norm(cross_e1_e2)

    # Compute the unit vector
    n_hat = cross_e1_e2 / norm
    
    # Compute A(T)
    At = (np.dot(cross_e1_e2, n_hat)) / 2

    # Compute A(T1)
    cross_e1_d3 = np.cross(e1, d3)
    At1 = (np.dot(cross_e1_d3, n_hat)) / 2

    # Compute A(T2)
    cross_e2_d1 = np.cross(e2, d1)
    At2 = (np.dot(cross_e2_d1, n_hat)) / 2

    # Compute A(T3)
    cross_e3_d2 = np.cross(e3, d2)
    At3 = (np.dot(cross_e3_d2, n_hat)) / 2
    
    b1 = At1/At
    b2 = At2/At
    b3 = At3/At
    
    fb1 = b1 * ftripoints[0]
    fb2 = b2 * ftripoints[1]
    fb3 = b3 * ftripoints[2]
    fb = fb1+fb2+fb3
    return  (b1,b2,b3), fb
  
  return  computer(p),computer


def rbfInterpolation(x = np.array([.8,.4,.6]),fx = np.array([1.64,1.16,1.36]), kernel='inverseDistance', lam = 1):
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