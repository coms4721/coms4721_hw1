from scipy.io import loadmat
import numpy as np
import pickle
import pandas as pd

news = loadmat('news.mat')

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
			# print "weights shape:", w.shape, "bias shape:", b.shape, "x shape:", x.shape
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

vocab = {}
with open("news.vocab") as f:
    for key, line in enumerate(f):
    	key = key+1
    	val = line.replace("\n",'')
       	#(key, val) = line.split()
        vocab[int(key)] = val
# for key, value in vocab.iteritems():
# 	print key, value
group = {}
with open("news.groups") as f:
    for line in f:
       (val, key) = line.split()
       group[int(key)] = val
# print group

# paramTop = {}
# for key, value in params.iteritems():
# 	print key, ' - '#, value
# 	theWeights = value['weights']#.tolist()
# 	print type(theWeights)
# 	print theWeights
# 	words = theWeights.argsort()#.argsort()[-2:]#[::-1]
# 	#words = words[-2:]
# 	print words, type(words), words.shape
# 	paramTop[key] = {'top20words':words}
# 	print paramTop[key]

#dfv = pd.DataFrame(vocab)
#dfg = pd.DataFrame(group)

dfv = pd.read_csv("news.vocab",header=None)
dfv.columns = ['word']
dfv['vuid'] = dfv.index + 1

dfg = pd.read_csv("news.groups",header=None)
dfg.columns = ['topic'] #just delcare col names here
dfg['topic'] = dfg.topic.str.split(' ',1).str[0]
dfg['guid'] = dfg.index + 1

df = pd.DataFrame(params)
df = df.T
df['guid'] = df.index 

print df.head(20)
print dfv.head(20)
print dfg.head(20)

df = df.merge(dfg, on='guid', how='left')

print df.head(20)


dfw = df[['weights']]
#dfw = dfw.apply(lambda x: pd.Series(x.split(',')))

dfw = dfw['weights'].tolist()

df_list = []

#dfw = pd.DataFrame(dfw)


for i, k in enumerate(dfw):
	j = k.tolist()
	df = pd.DataFrame(j)
	df = df.T
	df.columns = ['values']
	df['guid'] = i + 1
	df['vuid'] = df.index + 1
	df = df.sort('values', ascending=False).head(20)


	print df.head(25)


	df_list.append(df)
	
	

df = pd.concat(df_list)

df = df.merge(dfv, on='vuid', how='left').merge(dfg, on='guid', how='left')
#df['guid'] = df.index + 1

#df = df.T

print df.head(25)
#print dfw#.head(20)
#df = df.groupby(['guid','vuid','word','topic']).head(20).reset_index(drop=True)

df.to_csv('hw1-2.csv',index=False)
#print df.head(25)

#print paramTop
# the weights, there's 60,000, find top 20 
# grab top 20 indices in an array
# sort

# for i in news.groups:
# 	print the top 20 words. 


