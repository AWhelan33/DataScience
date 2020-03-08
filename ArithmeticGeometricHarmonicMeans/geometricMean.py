#Example of calculating Geometric mean
from scipy.stats import gmean
#define the dataset
data = [1,2,3,40,50,60,0.7,0.88,0.9,1000]
#calculate the mean
result = gmean(data)
print('Geometric Mean: %.3f' % result)
