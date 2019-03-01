import numpy as np
import pandas as pd
from scipy import signal
from scipy import misc

# Define your patterns here
CROSS = np.reshape(list('F*F*X*F*F'), (3, 3))
BEND  = np.reshape(list('F**F**XXX'), (3, 3))
ARROW = np.reshape(list('S*WSW*SSS'), (3, 3))

# Storing patterns in a dict
P = {'CROSS': CROSS, 'BEND': BEND, 'ARROW': ARROW}

def preprocess_pattern(inpattern) -> np.ndarray:
  output = inpattern.copy()
  vfunc = np.vectorize(lambda x: 0 if x == '*' else ord(x))
  output = vfunc(output).astype(np.int32)
  return output

def pattern_match_number(pattern) -> int:
  return np.sum(pattern**2)

def preprocess_input(matrix) -> np.ndarray:
  vfunc = np.vectorize(lambda x: ord(x))
  return vfunc(matrix).astype(np.int32)

def elementwise_check(sliceM, pattern) -> bool:
  sliceM = sliceM.reshape(-1)
  pattern = pattern.reshape(-1)
  return all([True if (y == 0) else x==y for x, y in zip(sliceM, pattern)])
  
def pattern_matching(matrix) -> (bool, list):
  matched = False
  matched_list = []
  matrix = preprocess_input(matrix)
  
  for pname in P:
    current_pattern = preprocess_pattern(P[pname])
    match_key = pattern_match_number(current_pattern)
    
    c2d = signal.correlate2d(matrix, current_pattern, mode='same')
    candidates = zip(*np.where(c2d==match_key))
    
    for cd in candidates:
      x, y = cd
      w, h = current_pattern.shape
      sliceM = matrix[x-1:x-1+w, y-1:y-1+h]
      if (elementwise_check (sliceM, current_pattern)):
        matched_list.append([pname, (x-1, y-1)])
        matched = True
  return matched, matched_list

def highlight_match(s) -> str:
  color = 'palegreen'
  return 'background-color: %s' % color