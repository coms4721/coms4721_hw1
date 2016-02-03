from scipy.io import loadmat
ocr = loadmat('ocr.mat')

import matplotlib.pyplot as plt
from matplotlib import cm

plt.imshow(ocr['data'][0].reshape((28,28)), cmap = cm.gray_r)
plt.show()

plt.imshow(ocr['testdata'][0].reshape((28,28)), cmap = cm.gray_r)
plt.show()

# Write a function that implements the 1-nearest neighbor classier with Euclidean distance.
# Your function should take as input a matrix of training feature vectors X and a vector of the
# corresponding labels Y, as well as a matrix of test feature vectors test. 

import numpy as np

np.matrix([[1, 2], [3, 4]])


z = np.column_stack((ocr['data'], ocr['labels']))

print z

# The output should be a
# vector of predicted labels preds for all the test points. Naturally, you should not use (or look at the
# source code for) any library functions for computing Euclidean distances, nearest neighbor queries,
# and so on. If in doubt about what is okay to use, just ask.
# For effciency, you should use vector operations (rather than, say, a bunch of for-loops). See
# http://www.mathworks.com/help/matlab/matlab_prog/vectorization.html to learn how to
# do this in MATLAB.
# Instead of using your 1-NN code directly with data and labels as the training data, do the
# following. For each value n 2 f1000; 2000; 4000; 8000g,

# Draw n random points from data, together with their corresponding labels. In matlab,
# use sel = randsample(60000,n) to pick the n random indices, and data(sel,:) and
# labels(sel) to select the examples; in Python, use sel = random.sample(xrange(60000),n)
# (after import random), ocr['data'][sel], and ocr['labels'][sel].

# import random
# sel = random.sample(xrange(60000),n)

# ocr['data'][sel]
# ocr['labels'][sel]


# Use these n points as the training data and test data as the test points, and compute the
# test error rate of the 1-NN classier.

# A plot of the error rate (on the y-axis) as a function of n (on the x-axis) is called a learning curve.
# We get an estimate of this curve by using the test error rate in place of the (true) error rate.

# Since the above process involves some randomness, you should repeat it independently several
# times (say, at least ten times). 


# Produce an estimate of the learning curve plot using the average of
# these test error rates (that is, averaging over the repeated trials). Add error bars to your plot that
# extend to one standard deviation above and below the means. Ensure the plot axes are properly
# labeled. Submit the plot and your source code.