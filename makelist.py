import numpy as np

def makelist(poly):
   n = poly.shape[2]
   points = poly[:, :, 0]

  for i in range (1,n):
      points = np.column_stack((points, poly[:, 1:, i]))

return points 
