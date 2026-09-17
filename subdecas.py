import numpy as np
def subdecas(cpoly):
  b0 = cpoly[:,0]
  b1 = cpoly[:,1]
  b2 = cpoly[:,2]
  b3 = cpoly[:,3]


b01 = (b0 + b1) /2
b11 = (b1 + b2) /2
b21 = (b2 + b3) /2

b02 = (b01 + b11) /2
b12 = (b11 + b21) /2

b03 = (b02 + b12) /2 

ud = np.column_stack((b0, b01, b02, b03))

ld = np.column_stack((b03, b12, b21, b3))

return ud, ld
