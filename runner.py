from sort import *
from compare import *
from evalMetrics import *
import matplotlib.pyplot as plot

def getMetricValue(sortAlgo, comp, metric, numTrials = 1000, listLen = 100):
	metricSum = 0
	for _ in range(numTrials):
		l = [i for i in range(listLen)]
		random.shuffle(l)
		metricSum += metric.getScore(sortAlgo.sort(l, comp))
	return metricSum / numTrials

# allSortAlgos = [BubbleSort(), QuickSort(), RegularSeasonSort()]
allSortAlgos = [BubbleSort(), SelectionSort(), InsertionSort(), QuickSort(), MergeSort(), HeapSort(), ShellSort(), GnomeSort(), RegularSeasonSort()]

metric = InversionMetric()

maxNoise = 50
noiseStep = 1
numTrialsPerDatum = 1000

for sortAlgo in allSortAlgos:
	metricValues = []
	for noiseRate in range(0, maxNoise + 1, noiseStep):
		comp = Comparator(noiseRate / 100)
		metricValues.append(getMetricValue(sortAlgo, comp, metric, numTrials = numTrialsPerDatum))
		print("%s %d %f" % (sortAlgo.getSortName(), noiseRate, metricValues[-1]))
	plot.plot([i / 100 for i in range(maxNoise + 1)], metricValues, label = sortAlgo.getSortName())
plot.legend()
plot.xlabel("Noise Rate")
plot.ylabel("Inversion Score")
plot.savefig("graph.png")
plot.show()