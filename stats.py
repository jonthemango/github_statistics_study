import math
from main import loadJsonFile, writeJsonFile

EXPLICIT_DATA_SET = loadJsonFile('reports/explicit_data.json')
IMPLICIT_DATA_SET = loadJsonFile('reports/implicit_data.json')
SAMPLE_DATA_SET = loadJsonFile('reports/sample_data.json')

N = len(SAMPLE_DATA_SET)
P = len(EXPLICIT_DATA_SET) / N


## Calculating proper sample variance
runningSum = 0
for data in SAMPLE_DATA_SET:
    x = 0
    if data in EXPLICIT_DATA_SET:
        x = 1
    runningSum += (x-P)**2

sampleVariance = runningSum/N


MEAN = P
STANDARD_DEVIATION = math.sqrt(sampleVariance)
MEDIAN = 1

data = {
    "Sample Mean" : MEAN,
    "Sample Variance" : sampleVariance,
    "Sample Standard Deviation" : STANDARD_DEVIATION,
    "Sample Median" : MEDIAN,
    "N": N,
    "P": P
}
writeJsonFile('reports/statistics.json', data)

from scipy.stats import binom
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

x = range(N-1)
rv = binom(N, P)
print(N,P)
expected_rb = binom(N, 0.5)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=10)  
ax.legend(loc='best', frameon=False)  
plt.suptitle('Probablity of Explicitily Typed Languages')
plt.ylabel("pmf")       
plt.xlabel("# of projects that are explicitly typed")      
plt.show()


