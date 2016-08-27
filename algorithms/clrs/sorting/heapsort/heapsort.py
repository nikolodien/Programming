#!/usr/bin/python

class Heap(object):
	length, arr = 0, None

	def __init__(self, array):
		self.length = len(array)
		self.arr = array

	def leftof(self, x):
		return x*2+1

	def rightof(self, x):
		return x*2+2

	def maintainHeap(self, i):
		left,right = self.leftof(i),self.rightof(i)
		largest = i
		if left<self.length and self.arr[i]<self.arr[left]:
			largest = left
		if right<self.length and self.arr[largest]<self.arr[right]:
			largest = right
		if not largest==i:
			self.arr[i],self.arr[largest]=self.arr[largest],self.arr[i]
			self.maintainHeap(largest)

	def maxHeapify(self):
		for i in range(self.length,-1,-1):
			self.maintainHeap(i)

	def sort(self):
		self.maxHeapify();
		while(self.length>0):
			self.arr[self.length-1],self.arr[0] = self.arr[0],self.arr[self.length-1]
			self.length = self.length-1
			self.maintainHeap(0)

	def display(self):
		print self.arr

heap = Heap([0, 9, 5, 100, -3, 5, -8, -100, 1000])
heap.sort()
heap.display()