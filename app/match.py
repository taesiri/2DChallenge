import numpy as np
import pandas as pd
from scipy import signal
from scipy import misc

# Define your patterns here
CROSS = np.reshape(list('F.F.X.F.F'), (3, 3))
BEND  = np.reshape(list('F..F..XXX'), (3, 3))
ARROW = np.reshape(list('S.WSW.SSS'), (3, 3))

# Storing patterns in a dict
P = {'CROSS': CROSS, 'BEND': BEND, 'ARROW': ARROW}

def elementwise_check(sliceM, pattern) -> bool:
  if (sliceM.shape != pattern.shape):
    return (False, '')
  
  sliceM = sliceM.reshape(-1)
  pattern = pattern.reshape(-1)
  return all([x==y for x, y in zip(sliceM, pattern)])
  
def pattern_matching(matrix) -> (bool, str):
  # clear up th input matrix
  matrix = np.array(matrix)
  try:
    matrix = matrix[~np.all(matrix=='.', axis=1)] # Removing empty rows
    matrix = matrix[:, ~np.all(matrix=='.', axis=0)] # Removing empty columns
  except:
    # Either the matrix is in bad shape or it only contains '.' chars
    return (False, '')

  matched_list = []
  
  for pkey in P:
    if elementwise_check(matrix, P[pkey]): matched_list.append(pkey)
    
  return (True, matched_list[0]) if len(matched_list) == 1 else (False, '')