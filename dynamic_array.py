import ctypes

class DynamicArray:


	def __init__(self):
		self._n = 0 # count the the actual elements
		self._capacity = 1 # defualt size of the arry
		self._A = self._make_array(self._capacity)

	def __len__(self):
		return self._n


	def __getitem__(self, k):
		if not 0 <= k < self._n:
			raise IndexError('Invalid index')
		return self._A[k]


	def append(self,obj):
		if self._n == self._capacity: # not enough room
			self._resize(2 * self._capacity) # double the capacity
		self._A[self._n] = obj # append the Element in the end
		self._n += 1


	def remove(self, value):
		'''Remove first occurrence of value (or raise ValueError).'''
		# note: im not consider shrinking the dynamic array in this version
		for k in range(self._n):
			if self._A[k] == value:
				for j in range(k, self._n-1):
					self._A[j] = self._A[j+1]
				self._A[self._n-1] = None
				self._n -= 1
			
		raise ValueError('value not found')


	def insert(self, k, value):
		''' insert value at index k'''
		if self._n == self._capacity:
			self._resize(2 * self._capacity)
		for j in range(self._n, k, -1):
			self._A[j] = self._A[j-1]
		self._A[k] = value
		self._n += 1


	def _resize(self, c):
		""" resize the array to capacity c"""
		B = self._make_array(c)

		for k in range(self._n): # for each existing value
			B[k] = self._A[k]
		self._A = B              # using the bigger array
		self._capacity = c


	def _make_array(self, c):
		""" make new low level array"""
		return (c * ctypes.py_object)()


		