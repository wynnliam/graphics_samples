# 2D Convolution
This sample is taken from the following source:

*Chapter 9 - Signal Processing, Fundamentals of Computer Graphics - 4th Edition* by Marschner and Shirley

This sample shows how one can extend the concept of Convolution to 2D. In fact, you could go to higher
dimensions if you wanted. However, 2D is both simple and has practical uses in texture processing. The
gist is you have a 2D sequence (say a texture, or a matrix): so it has `N x M` dimensions, and you have
a smaller filter that is also 2D. For a given point on the matrix, you compute the weighted sum of the
points around it using the filter.

