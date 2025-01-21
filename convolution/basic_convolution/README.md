# Convolution
This sample is taken from the following source:

*Chapter 9 - Signal Processing, Fundamentals of Computer Graphics - 4th Edition* by Marschner and Shirley

This sample covers basic convolution. Convolution is an operator over two functions `a`, `b` expressed as
`conv(a, b)`[1]. The idea is that we are taking some sequence `a`, and applying a filter `b` to it, which
creates a sequence `c` that is the weighted moving average of the values in `a`. That is, for a given value `v`
in `a`, we take the average of each value around `v` (as well as `v`), scaled by a correpsonding weight `w` in
`b`. For example, consider a trivial sequence `a`:

`a = [0, 1, 2, 3, 4, 5, 6]`

And a trivial filter `b`:

`b = [0, 0.2, 0.2, 0.2, 0.2, 0.2, 0]`

Now to compute `conv(a, b)[3]`, we would do the following:

```
conv(a, b)[3] = 0.2 * 1 + 0.2 * 2 + 0.2 * 3 * 0.2 * 4 + 0.2 * 5
conv(a, b)[3] = 0.2 + 0.4 + 0.6 + 0.8 + 1 = 3
```

While simple, convolution has many use cases in graphics, machine learning, signal processing, and more. I invite
you to run the sample `convolution.py` and see how it works. Try defining your own sequences and filters and seeing
the result!


[1] - Note that I am not using the Marschner and Shirley notation due to the lack of fancy symbols I am
too lazy to employ here in a README.
