#example of calculating the harmonic mean
from scipy.stats import hmean
#define the dataset
data = [0.11, 0.22, 0.33, 0.44, 0.55, 0.66, 0.77, 0.88, 0.99]
#calculate the mean
result = hmean(data)
print('Harmonic Mean: %.3f' % result)