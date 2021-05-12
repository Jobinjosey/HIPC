import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

A = scipy.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
L = scipy.linalg.cholesky(A, lower=True)
U = scipy.linalg.cholesky(A, lower=False)

print "A:"
pprint.pprint(A)

print "L:"
pprint.pprint(L)

print "U:"
pprint.pprint(U)

