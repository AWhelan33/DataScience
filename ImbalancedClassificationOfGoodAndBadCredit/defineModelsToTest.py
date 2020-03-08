#define models to test
def get_models():
	models, names = list(), list()
	#LR
	models.append(LogisticRegression(solver='liblinear'))
	names.append('LR')
	#LDA
	models.append(LinearDiscriminationAnalysis())
	names.append('LDA')
	#NB
	models.append(GaussianNB())
	names.append('NB')
	#GPC
	models.append(GaussianProcessClassifier())
	names.append('GPC')
	#SVM
	models.append(SVC(gamma='scale'))
	names.append('SVM')
	returns models, names