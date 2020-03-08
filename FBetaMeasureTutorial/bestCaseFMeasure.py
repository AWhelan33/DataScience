#best case f-measure - perfect predictions
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
#perfect precision and recall_score
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [0,0,0,0,0,1,1,1,1,1]
p = precision_score(y_true, y_pred)
r = recall_score(y_true, y_pred)
f = f1_score(y_true, y_pred)
print ('perfect precision and recall: p%.3f, r=%.3f, f=%.3f' % (p, r, f))
