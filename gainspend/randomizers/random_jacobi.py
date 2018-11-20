def generate_jacobi(m, x0=None, eps=1e-5, max_iteration=100):
  """
  Parameters
  ----------
  m  : list of list of floats : coefficient matrix
  x0 : list of floats : initial guess
  eps: float : error tolerance
  max_iteration: int

  Returns
  -------
  list of floats
      solution to the system of linear equation

  Raises
  ------
  ValueError
      Solution does not converge
  """
  n  = height(m)
  x0 = [0] * n if x0 == None else x0
  x1 = x0[:]

  for __ in range(max_iteration):
    for i in range(n):
      s = sum(-m[i][j] * x1[j] for j in range(n) if i != j)
      x1[i] = (m[i][n] + s) / m[i][i]
    if all(abs(x1[i]-x0[i]) < eps for i in range(n)):
      return x1
    x0 = x1[:]
  raise ValueError('Solution does not converge')

def column(m, c):
    return [m[i][c] for i in range(len(m))]

def row(m, r):
    return m[r][:]

def height(m):
    return len(m)

def width(m):
    return len(m[0])


# if __name__ == '__main__':
#   m =  [[4,3,9,1,4],  [8,3,2,4],  [9,8,5,4]]
#   print(gauss_seidel(m))
