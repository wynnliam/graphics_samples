# Liam Wynn, 1-21-2025, Graphics Samples: Reconstruction

#
# Performs basic 2D convolution using both a discrete
# sequence, and discrete filter.
#

import numpy as np

# 2D sequence.
a = np.array([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
])

# 2D filter. This is an averaging filter
f = np.array([
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1]
]) / 9

#
# Evaluates the convolution of a and f at point
# (i, j).
#

def convolve2d(a, f, i, j):

  #
  # Dimensions of a
  #

  a_h = a.shape[0]
  a_w = a.shape[1]

  #
  # Dimensions of f
  #

  f_h = f.shape[0]
  f_w = f.shape[1]

  #
  # Dimensions to add to a to pad it so that the filter
  # can be applied to edge cases. Say at the leftmost column of a,
  # you will have half of the filter sticking off the edge. Also
  # for the rightmost, topmost, and bottommost edges.
  #

  pad_h = f_h // 2
  pad_w = f_w // 2

  #
  # Now define a padded version of a. Everything that is not from a is
  # set to 0.
  #

  padded_a = np.pad(a, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=(0,0))

  #
  # Extract the region centered around (i, j)
  #

  region = padded_a[i:i + f_h, j:j + f_w]

  #
  # Now compute the result!
  #

  result = np.sum(region * f)
  return result


print(f"a = {a}")
print(f"f = {f}")

i = 1
j = 1
result = convolve2d(a, f, i, j)

print(f"Convolution result at index ({i}, {j}): {result}")
