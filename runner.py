from sort import *
from compare import *
from evalMetrics import *

noiseRate = 0.10
comp = Comparator(noiseRate)

algo = RegularSeasonSort()
l = [i for i in range(100)]
random.shuffle(l)

# print(l)
sortedL = algo.sort(l, comp)
print(sortedL)
# print(l)

print(InversionMetric().getScore(sortedL))