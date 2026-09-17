from subdivstep import subdivstep

def itersubdiv (poly, n):

  for i in range(n):
    poly = subdivstep(poly)

return poly
