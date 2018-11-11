import math
from main import loadJsonFile, writeJsonFile

EXPLICIT_DATA_SET = loadJsonFile('reports/explicit_data.json')
IMPLICIT_DATA_SET = loadJsonFile('reports/implicit_data.json')
SAMPLE_DATA_SET = loadJsonFile('reports/sample_data.json')


N = len(SAMPLE_DATA_SET)
P =  len(EXPLICIT_DATA_SET) / N

MEAN = N*P
VARIANCE = MEAN * (1 - P)
STANDARD_DEVIATION = math.sqrt(VARIANCE)
MEDIAN = math.floor(MEAN)

data = {
    "Mean" : MEAN,
    "Variance" : VARIANCE,
    "Standard Deviation" : STANDARD_DEVIATION,
    "Median" : MEDIAN
}


from scipy.stats import binom
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

x = range(N-1)
rv = binom(N, P)
print(N,P)
expected_rb = binom(N, 0.5)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=10,label='Probablity of Explicitily Typed Languages')  
ax.legend(loc='best', frameon=False)          
plt.show()


writeJsonFile('reports/statistics.json', data)