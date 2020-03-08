#intuition for precision
from sklearn.metrics import precision_score

#no precision
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [0,0,0,0,0,0,0,0,0,0]
score = precision_score(y_true, y_pred)
print ('No Precision: %.3f' % score)
# some false positives
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [0,0,0,1,1,1,1,1,1,1]
score = precision_score(y_true, y_pred)
print ('Some false positives: %.3f' % score)
# some false negatives 
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [0,0,0,0,0,0,0,1,1,1]
score = precision_score(y_true,y_pred)
print('Some False Negatives: %.3f' % score)
#perfect precision
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [0,0,0,0,0,1,1,1,1,1]
score = precision_score(y_true, y_pred)
print ('perfect precision: %.3f' % score)