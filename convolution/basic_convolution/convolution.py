# Liam Wynn, 1-12-2025, Graphics Samples: Convolution

#
# Defines a basic convolution operator over a discrete, 1D sequence.
# The user supplies a sequence a, and a filter b, and an index i,
# and the convolve function will print the result.
#
# To define a filter, the user chooses a radius r and a lambda on
# a value k, and if -r <= k <= r, we retun the lambda applied to
# k, otherwise we return 0.
#

#
# Defines a simple box filter lambda. The user gives a radius
# r, and this routine returns a simple box filter b defined as
# 1 / (2 * r + 1) for all values k such that -r <= k <= r, otherwise
# 0.
#
# For ease of use in the convolution operator, we also return the
# radius. So for whatever filter you define, please observe this
# pattern.
#

def box_filter(r):
  b = lambda k : (1 / (2 * r + 1)) if -r <= k and k <= r else 0
  return { "op": b, "radius": r }

#
# Performs convolution on a 1D, discrete sequence a, using
# filter b, at index i.
#

def convolve(a, b, i):
  s = 0
  r = b["radius"]
  op = b["op"]
  lo_bound = i - r
  hi_bound = i + r
  mx_bound = len(a) - 1

  for j in range(lo_bound, hi_bound + 1):
    if 0 <= j and j <= mx_bound:
      s += a[j] * op(i - j)

  return s

a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
b = box_filter(2)

for i in range(0, 10):
  print(i, a[i], convolve(a, b, i))
