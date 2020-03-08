#calculate the f0.5 measure
from sklearn.metrics import fbeta_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

#perfect precision, 50% recall
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [1,1,1,1,1,1,1,1,1,1]
p = precision_score(y_true, y_pred)
r = recall_score(y_true, y_pred)
f = fbeta_score(y_true, y_pred, beta=0.5)
print ('Result: p=%.3f, r=%.3f, f=%.3f' % (p,r,f))
