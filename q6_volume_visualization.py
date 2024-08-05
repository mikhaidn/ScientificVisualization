import numpy as np
import numpy.linalg as la

def normalize(x = np.array([[-.1,.2,-.1]])):
  
  return x/np.linalg.norm(x)


#page 7
# https://d3c33hcgiwev3.cloudfront.net/vk2blDq8S9-Nm5Q6vBvfsQ_929f43bc10ec459a9b7a17ecbf8e6138_519-11-4-3.pdf?Expires=1719273600&Signature=CCKDQSSNarWnK6HzhPB-tl0sXphuyWEyxEJL3VIkzG-VzcFYxYQu~onvJOR3t7R44ZFZXAhVwg6QwTO58AmpUuZTu9E5eIvc3FMg0lN4s2mGJuFW4RIrTbcRqgQH4xJNldeiORd~Wda4pyI9Dbb6pyyYSaTxzQX9zbNKlU~rNOI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
def overFront(cf=np.array([.2,.8,.7]),af=1,cb=np.array([.4,1,.8]),ab=.1):
  c  = af*cf + (1-af)*ab*cb
  a = af + (1-af)*ab
  return (c,a)

def overBack(c,a,C):
  return a*c + (1-a)*C