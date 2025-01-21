# Liam Wynn, 1-21-2025, Graphics Samples: Reconstruction

#
# Defines a simple program that performs discrete-continuous convolution.
# Specifically, we looking at taking a discrete sequence a and making it
# continuou using a gaussian filter f(x) = e^(-x^2).
#

import numpy as np

#
# Defines a simple discrete sequence a = [1, 2, 3, 4]
#

a = [1, 2, 3, 4]

#
# Defines a simple continuous filter - gaussian.
#

def f(k):
  return np.exp(-k ** 2)

def reconstruct(a, f, x):
  s = 0
  for n in range(len(a)):
    s += a[n] * f(x - n)

  return s

#
# So we have a discrete sequence a = [1, 2, 3, 4]. If we are making
# it continuous, the benefit is we can ask questions like, "what is
# the value of a[1.5]? Of course, a[1.5] doesn't exist, but we
# reconstruct it by using a filter f to compute it.
#
 
x = 1.5
result = reconstruct(a, f, x)
print(f"Reconstruction result at x = {x}: {result}")
