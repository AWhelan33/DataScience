#worst case f-measure false positives
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
#no precision or recall
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [1,1,1,1,1,0,0,0,0,0]
p = precision_score(y_true, y_pred)
r = recall_score(y_true, y_pred)
f = f1_score(y_true, y_pred)
print ('No precision or recall false positives : p=%.3fm r=%.3f, f=%.3f' %(p,r,f)) 

#another worst case f measure false negatives
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [0,0,0,0,0,0,0,0,0,0]
print ('No Precision or Recall False Negatives: p=%.3f, r=%.3f, f=%.3f' %(p,r,f))