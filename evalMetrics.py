class SortMetric():
	def getScore(self, arr):
		raise NotImplementedError("A SortMetric must implement getScore()")

class InversionMetric(SortMetric):
	def getScore(self, arr):
		n = len(arr)
		numInversions = 0
		for i in range(n):
			for j in range(i + 1, n):
				if arr[i] > arr[j]: numInversions += 1
		return numInversions / (n * (n - 1) / 2)		