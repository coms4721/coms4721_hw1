from scipy.io import loadmat
ocr = loadmat('ocr.mat')

import matplotlib.pyplot as plt
from matplotlib import cm

import random
import numpy as np

import datetime 
import csv
#plt.imshow(ocr['data'][0].reshape((28,28)), cmap = cm.gray_r)
#plt.show()

def dist(x, y):
	diff = x.astype(np.float32) - y.astype(np.float32)
	return diff.dot(diff)	

def nnClassifier(trainingData, trainingLabels, testData, testLabels):
	total_count = len(testLabels)
	wrong_count = 0
	for testVector, testLabel in zip(testData, testLabels):
		# find the closest training vector
		minDist = float('inf')
		minLabel = None
		for trainingVector, trainingLabel in zip(trainingData, trainingLabels):
			d = dist(testVector, trainingVector)
			#print 'd:', d, 'minDist:', minDist
			if d < minDist:
				minDist = d
				minLabel = trainingLabel

		# check if minLabel is correct
		# print 'minLabel:', minLabel[0], 'trainingLabel:', trainingLabel[0], 'testLabel:', testLabel[0]
		#print testLabel[0]
		if minLabel[0] != testLabel[0]:
			wrong_count += 1
		
	print 'wrongcount:', wrong_count
	errorRate = float(wrong_count) / total_count
	print errorRate
	return errorRate

testData = ocr['testdata']
testLabels = ocr['testlabels']

#z = 1000 #for testing set z at 100
#save data to csv after loop, do it 10 times. change sample_sizes back and remove selz

sample_sizes = [1000,2000,4000,8000]
#sample_sizes = [100,200,400,800]

for i in range(10):
	dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	dt = dt.replace(' ','-').replace(':','-')
	print dt

	error_rates = []
	for n in sample_sizes:
		print n
		sel = random.sample(xrange(60000),n)
		trainingData = ocr['data'][sel]
		trainingLabels = ocr['labels'][sel]

		# selz = random.sample(xrange(10000),z)
		# testData = ocr['testdata'][selz]
		# testLabels = ocr['testlabels'][selz]

		e = nnClassifier(trainingData, trainingLabels, testData, testLabels)
		error_rates.append(e)

	print error_rates

	with open("data/output"+dt+".csv", "wb") as f:
		writer = csv.writer(f)
		row = sample_sizes, error_rates
		writer.writerows(row)

# TAKES ABOUT [Finished in 21415.4s] ABOUT 5.948722222 HOURS

#plt.plot(sample_sizes, error_rates)
#plt.show()

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