from compare import *
import copy
import random
import math

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

class SortAlgo():
	def sort(self, arr, comp):
		raise NotImplementedError("A SortAlgo must implement the sort() function")

class BubbleSort(SortAlgo):
	def sort(self, arr, comp):
		arr = copy.deepcopy(arr)

		for i in range(len(arr)):
			for j in range(len(arr) - i - 1):
				if comp.greaterThan(arr[j], arr[j + 1]):
					swap(arr, j, j + 1)
		return arr

class SelectionSort(SortAlgo):
	def sort(self, arr, comp):
		arr = copy.deepcopy(arr)

		for i in range(len(arr)):
			minIndex = i

			for j in range(i + 1, len(arr)):
				if comp.lessThan(arr[j], arr[minIndex]): minIndex = j
			swap(arr, i, minIndex)
		return arr

class InsertionSort(SortAlgo):
	def sort(self, arr, comp):
		arr = copy.deepcopy(arr)

		for i in range(1, len(arr)):
			j = i
			while j > 0 and comp.greaterThan(arr[j - 1], arr[j]):
				swap(arr, j, j - 1)
				j -= 1
		return arr

class QuickSort(SortAlgo):
	def sort(self, arr, comp):
		def sortSub(minIndex, maxIndex):
			if minIndex >= maxIndex: return

			swap(arr, random.randint(minIndex, maxIndex), maxIndex)
			
			currIndex = minIndex
			nextHiIndex = maxIndex - 1

			while currIndex <= nextHiIndex:
				if comp.lessThan(arr[currIndex], arr[maxIndex]):
					currIndex += 1
				else:
					swap(arr, currIndex, nextHiIndex)
					nextHiIndex -= 1

			swap(arr, currIndex, maxIndex)

			sortSub(minIndex, currIndex - 1)
			sortSub(currIndex + 1, maxIndex)

		arr = copy.deepcopy(arr)
		sortSub(0, len(arr) - 1)
		return arr

class MergeSort(SortAlgo):
	def sort(self, arr, comp):
		def sortSub(minIndex, maxIndex):
			if minIndex == maxIndex: return [arr[minIndex]]

			midIndex = (minIndex + maxIndex) // 2

			sortedFront = sortSub(minIndex, midIndex)
			sortedBack = sortSub(midIndex + 1, maxIndex)

			sortedFull = []
			while len(sortedFront) > 0 and len(sortedBack) > 0:
				if comp.lessThan(sortedFront[0], sortedBack[0]):
					sortedFull.append(sortedFront.pop(0))
				else:
					sortedFull.append(sortedBack.pop(0))
			if len(sortedFront) > 0:
				return sortedFull + sortedFront
			else:
				return sortedFull + sortedBack

		arr = copy.deepcopy(arr)
		return sortSub(0, len(arr) - 1)

class HeapSort(SortAlgo):
	def sort(self, arr, comp):
		def parent(i): return math.floor((i - 1) / 2)
		def leftChild(i): return 2 * i + 1
		def rightChild(i): return 2 * i + 2
		def bubbleUp(i):
			while i > 0:
				p = parent(i)
				if comp.greaterThan(arr[i], arr[p]): return
				swap(arr, i, p)
				i = p

		arr = copy.deepcopy(arr)

		# heapify
		for i in range(len(arr)):
			bubbleUp(i)

		sortedArr = []
		while len(arr) > 0:
			sortedArr.append(arr[0])

			lastVal = arr.pop(-1)
			if len(arr) == 0: break
			arr[0] = lastVal

			# trickle down
			i = 0
			while i < len(arr):
				l = leftChild(i)
				r = rightChild(i)

				if l >= len(arr): break
				elif r < len(arr):
					minChildIndex = l if comp.lessThan(arr[l], arr[r]) else r
				else:
					minChildIndex = l

				if comp.lessThan(arr[minChildIndex], arr[i]):
					swap(arr, minChildIndex, i)
					i = minChildIndex
				else: 
					break
		return sortedArr

class ShellSort(SortAlgo):
	def __init__(self, gapSequence = [1,4, 10, 23, 57, 132, 301, 701]):
		super(ShellSort, self).__init__()
		self.gapSequence = gapSequence

	def sort(self, arr, comp):
		arr = copy.deepcopy(arr)
		for g in range(len(self.gapSequence) - 1, -1, -1):
			gap = self.gapSequence[g]
			for i in range(gap, len(arr)):
				temp = arr[i]
				j = i
				while j > gap - 1 and comp.greaterThan(arr[j - gap], temp):
					arr[j] = arr[j - gap]
					j -= gap
				arr[j] = temp

		return arr

class CombSort(SortAlgo):
	def __init__(self, shrinkFactor = 1.3):
		super(CombSort, self).__init__()
		self.shrinkFactor = shrinkFactor

	def sort(self, arr, comp):
		arr = copy.deepcopy(arr)

		gap = len(arr)
		listSorted = False

		while not listSorted:
			gap = math.floor(gap / self.shrinkFactor)
			if gap > 1:
				listSorted = False
			else:
				gap = 1
				listSorted = True

			for i in range(0, len(arr) - gap):
				if comp.greaterThan(arr[i], arr[i + gap]):
					swap(arr, i, i + gap)
					listSorted = False
		return arr

class GnomeSort(SortAlgo):
	def sort(self, arr, comp):
		arr = copy.deepcopy(arr)

		i = 0
		while i < len(arr):
			if i == 0 or comp.greaterThan(arr[i], arr[i - 1]):
				i += 1
			else:
				swap(arr, i, i - 1)
				i -= 1
		return arr

class RegularSeasonSort(SortAlgo):
	def sort(self, arr, comp):
		arr = copy.deepcopy(arr)

		numSmallerMap = {v: 0 for v in range(len(arr))}
		for i in range(len(arr)):
			for j in range(i + 1, len(arr)):
				if comp.lessThan(arr[i], arr[j]):
					numSmallerMap[j] += 1
				else:
					numSmallerMap[i] += 1

		sortedList = []
		while len(numSmallerMap) > 0:
			minIndex = -1
			for ind in numSmallerMap:
				if minIndex == -1 or numSmallerMap[ind] < numSmallerMap[minIndex]:
					minIndex = ind
			sortedList.append(arr[minIndex])
			del numSmallerMap[minIndex]

		return sortedList
