from compare import *
import copy

class SortAlgo():
	def sort(self, arr, comp):
		raise NotImplementedError("A SortAlgo must implement the sort() function")

class BubbleSort(SortAlgo):
	def sort(self, arr, comp):
		arr = copy.deepcopy(arr)

		for i in range(len(arr)):
			for j in range(len(arr) - i - 1):
				if comp.greaterThan(arr[j], arr[j + 1]):
					temp = arr[j + 1]
					arr[j + 1] = arr[j]
					arr[j] = temp
		return arr