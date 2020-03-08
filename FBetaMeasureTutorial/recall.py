# intuition for recall
from sklearn.metrics import recall_score

# no recall
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [0,0,0,0,0,0,0,0,0,0]
score = recall_score(y_true, y_pred)
print ('No recall: %.3F' % score)
# some false positives
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [0,0,0,1,1,1,1,1,1,1]
score = recall_score(y_true, y_pred)
print ('Some False Positives: %.3f' % score)
# some false negatives
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [0,0,0,0,0,0,0,1,1,1]
score = recall_score(y_true, y_pred)
print ('some false negatives: %.3f' % score)
#perfect recall\
y_true = [0,0,0,0,0,1,1,1,1,1]
y_pred = [0,0,0,0,0,1,1,1,1,1]
score = recall_score(y_true, y_pred)
print ('perfect recal : %.3f' % score)