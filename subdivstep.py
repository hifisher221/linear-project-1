import numpy as np
from subdecas import subdecas

def subdivstep(lpoly):

  n = lpoly.shape[2]

newpoly = np.zeros((2,4,3 *n))

for i in range(n):

  ud, ld = subdecas(lpoly[:, :, i])

  newpoly[:, :, 2 * i] = ud
  newpoly[:, :, 2 * i + 1] = ld

return newpoly
