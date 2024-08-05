# from q5_contouring_marching_squares import *
import numpy as np
import numpy.linalg as la

# page 5 
# https://d3c33hcgiwev3.cloudfront.net/k9zLvIlOQZucy7yJTnGbLw_b5d635cb114e48bc9f5b8f3566b94aca_519-10-3.pdf?Expires=1719187200&Signature=WF9FO8SwqViME9~g7259BSrACmY9f1swaTKlGlXhdnEvhfRDgFyndA9eFoj9ys3X31kik8aSTNfOWcxjqSshiw81-RMmt3cfJ1MFbwXamRXcxjEkqBDmEyHaZBhm6TBOh2MNtF8nON0kdDZBb0dnSzEEqtbVoldwnmaPGUSsjfg_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
def dualMarchingSquares(points = np.array([[8,4],[8,5],[9,5],[9,4]]),
                        fx =np.array([22,44,92,56]),
                        thresh =92):
  # 0,0 is bottom left  -- br
  BOTTOM_LEFT_INDEX =0
  TOP_LEFT_INDEX = 1
  TOP_RIGHT_INDEX = 2
  BOTTOM_RIGHT_INDEX =3
  
  
  return "unimplemented"


def dualBipolarVerticies(bipolar1 = np.array([[5,11],[6,11]]),
                        fx1 =np.array([25,90]),
                        bipolar2 = np.array([[6,10], [6,11]]),
                        fx2 =np.array([61,90]),
                        thresh =70):
  t1 = la.norm(thresh-fx1[0])/la.norm(fx1[1]-fx1[0])
  intersection1 = (1-t1)*bipolar1[0]+t1*bipolar1[1]
  t2 = la.norm(thresh-fx2[0])/la.norm(fx2[1]-fx2[0])
  intersection2 = (1-t2)*bipolar2[0]+t2*bipolar2[1]
  
  dual = (intersection2+ intersection1)/2
  
  return dual
  

