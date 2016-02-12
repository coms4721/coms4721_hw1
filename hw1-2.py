from scipy.io import loadmat
news = loadmat('news.mat')

# vocab = 'news.vocab'
# group = 'news.groups'

news.to_csv()

#Two

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
		# mle = x_1.sum(axis=0) / cnt
		mu = (1 + x_1.sum(axis=0)) / ( 2 + cnt)
		pi = cnt/float(totCnt)
		bias = np.log(pi) - np.log(1 - mu).sum() #lgo pi + sum of all log minus meu
		weights = np.log(mu) - np.log(1 - mu) #log meu, log 1 - meu

		paramDict[theClass] = {'bias':bias, 'weights':weights}

	return paramDict


def get_error_rate(params, Xtest, Ytest):
	# which class has the highest w*x + b
	return 0

# def laplace():

# def mle():



	#len(np.where(y==4)[0])/float(len(y))



#(laplace | mle)
Xtrain = news['data']
Ytrain = news['labels']
params = get_params(Xtrain, Ytrain)

print "Training error:", get_error_rate(params, Xtrain, Ytrain)

Xtest = news['testdata']
Ytest = news['testlabels']

print "Test error:", get_error_rate(params, Xtest, Ytest)

# for i in news:
# 	print i
# 	for j in news['data']:
# 		print j