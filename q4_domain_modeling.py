# from q4_domain_modeling import *
import numpy as np
import numpy.linalg as la

# 7204
def rectilinearMeshStorage(grid = np.array([902,276,620]), nBytes = 4):
  numDimensions = len(grid) 
  numNums = np.sum(grid) + numDimensions
  return numNums * nBytes

# page 13
# https://d3c33hcgiwev3.cloudfront.net/Znjz-RFQTdu48_kRUP3bVQ_0829cd1d3b054bad871905611d6a6165_519-8-1.pdf?Expires=1719187200&Signature=RIMlP64ErQ8Bw-4fQsgiSshlAPHYFCcUsS0K0vJy8SE987ycLZ-uCijOcz904GtYLgckAwZUUMk63qNJk1KXLsiE6myT2i4tfh45q~GFFWcJMSC5vxDBKfK3YFblP-LEAycFd~h1F8r1XnP4DdeV7ZAZXQsFTmMoQDi--3jRCH0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
def curvilinearMeshStorage(grid = np.array([902,276,620]), nBytes = 4):
  numDimensions = len(grid) 
  numNums = (np.prod(grid) * numDimensions )+ numDimensions
  return numNums * nBytes


# page 4
# https://d3c33hcgiwev3.cloudfront.net/gOJRqXSlScuiUal0pfnLKA_1ddbf5b5fc64423db09cac6d209790e0_519-8-3.pdf?Expires=1719187200&Signature=blabDdi076KPBySWZI-XwHHLWQQSvGcd6yKDplIXSMp-PFOZBRcy-Q0wfYJNxUK3fMC7joiUfPaYN~RW4edehu1Sxrvw6jXhf4ZeJgrVdcSe9L5Wg3mVRnOHJBOkDbOZd5tsowtpZ3lS1d0y91qphB~wWwlwHHVVqzj7Ii3-RUY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
def tinMeshComparisionCount(v=9617,f=19230):
  unusedV =  v
  _ = unusedV
  NUM_VERTICIES_IN_TRIANGLE = 3
  return f *NUM_VERTICIES_IN_TRIANGLE 
  

class HalfEdge:
  # page 8
  # https://d3c33hcgiwev3.cloudfront.net/gOJRqXSlScuiUal0pfnLKA_1ddbf5b5fc64423db09cac6d209790e0_519-8-3.pdf?Expires=1719187200&Signature=blabDdi076KPBySWZI-XwHHLWQQSvGcd6yKDplIXSMp-PFOZBRcy-Q0wfYJNxUK3fMC7joiUfPaYN~RW4edehu1Sxrvw6jXhf4ZeJgrVdcSe9L5Wg3mVRnOHJBOkDbOZd5tsowtpZ3lS1d0y91qphB~wWwlwHHVVqzj7Ii3-RUY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
  def __init__(self):
    self.vertex = 1
    self.face =1
    self.halfNext= 2
    self.halfPrev = 0
    self.halfOpposite = 10
  
  
  