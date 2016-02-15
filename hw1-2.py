from scipy.io import loadmat
import numpy as np
import pickle

news = loadmat('news.mat')
# vocab = 'news.vocab'
# group = 'news.groups'
def get_params(Xtr, Ytr):
	# finding w and b for each class
	Ytr = Ytr.flatten()
	theClasses = set(Ytr)#list of classes
	totCnt = len(Ytr)
	paramDict = {}
	for theClass in theClasses:
		idx = np.where(Ytr==theClass)[0]
		cnt =  len(idx)
		xForThisClass = Xtr[idx] 
		mu = (1 + xForThisClass.sum(axis=0)) / ( 2 + cnt) #shoudl this be xForThisClass instead of x_1
		pi = cnt/float(totCnt)
		bias = np.log(pi) + np.log(1 - mu).sum() #lgo pi + sum of all log minus meu
		weights = np.log(mu) - np.log(1 - mu) #log meu, log 1 - meu
		paramDict[theClass] = {'bias':bias, 'weights':weights}
	return paramDict

def get_error_rate(params, Xtest, Ytest):
	#print "Xtest shape:", Xtest.shape
	#print "Ytest shape:", Ytest.shape
	total_count = len(Ytest)
	wrong_count = 0
	for testVector, testLabel in zip(Xtest, Ytest):
		#print testVector
		x = testVector
		maxLL = float('-inf')
		minLabel = None
		for key, value in params.iteritems():
			# make a prediction for input testVector
			w = value['weights']
			b = value['bias']
			# print "weights shape:", w.shape
			# print "bias shape:", b.shape
			# print "x shape:", x.shape
			# # np.dot(w, x) #### no! x is not a numpy array
			# # w.dot(x) ###### x is not a numpy array
			# # np.dot(w, x.to_array()) #### slow
			# # w.dot(x.to_array()) #### same
			# # x.dot(w)
			pred = x.dot(w.T) + b #should pred label 1-20? 
			# if this prediction != testLabel, increment wrong_count
			if pred > maxLL:
				maxLL = pred
				minLabel = key
		#print "minlable", minLabel.shape
		#print "Testlable", testLabel.shape
		# print type(minLabel), type(testLabel[0])
		if int(minLabel) != int(testLabel[0]):
			wrong_count += 1
		
	#print 'wrongcount:', wrong_count
	errorRate = float(wrong_count) / total_count
	#print errorRate
	return errorRate
	#which class has the highest w*x + b

Xtrain = news['data']
Ytrain = news['labels']
params = get_params(Xtrain, Ytrain)

#print "Training error:", get_error_rate(params, Xtrain, Ytrain)

Xtest = news['testdata']
Ytest = news['testlabels']
#print "Test error:", get_error_rate(params, Xtest, Ytest)

# print params

# pickle.dump( params, open( "save.p", "wb" ) )

paramTop = {}
for key, value in params.iteritems():
	print key, ' - '#, value
	theWeights = value['weights']#.tolist()
	print type(theWeights)
	print theWeights
	words = theWeights.argsort()#.argsort()[-2:]#[::-1]
	words = words[20:]
	print words, type(words), words.shape
	# paramTop[key] = {'top20words':words}
	# print paramTop[key]
#print paramTop
# the weights, there's 60,000, find top 20 
# grab top 20 indices in an array
# sort

# for i in news.groups:
# 	print the top 20 words. 


