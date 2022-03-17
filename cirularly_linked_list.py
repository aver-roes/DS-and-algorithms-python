
class Empty(Exception):
	pass



class circularlyQueue:

	class _Node:
		""" Lightweight, nonpublic class for storing a singly linked node """
		__slots__ = '_element', '_next' #streamline memory usage

		def __init__(self, element, next):
			self._element = element
			self._next = next


	def __init__(self):
		self._tail = None
		self._size = 0


	def __len__(self):
		return self._size


	def is_empty(self):
		return self._size == 0


	def first(self):

		if self.is_empty():
			raise Empty('Queue is Empty')
		head = self._tail._next
		return head._element


	def last(self):

		if self.is_empty():
			raise Empty('Queue is Empty')
		return self._tail._element


	def enqueue(self, e):

		newest = self._Node(e, None)
		if self.is_empty():
			newest._next = newest
		else:
			newest._next = self._tail._next
			self._tail._next = newest
		self._tail = newest
		self._size += 1


	def dequeue(self):

		if self.is_empty():
			raise Empty('Queue is Empty')

		old_head = self._tail._next

		if self._size == 1:
			self._tail = None
		else:
			self._tail._next = old_head._next

		self._size -= 1
		return old_head._element


	def rotate(self):
		"""Rotate front element to the back of the queue.
		
		NOTE: rotate is useful when implementing Round-Robin Schedulers."""
		if self._size > 0:
			self._tail = self._tail._next



queue = circularlyQueue()

queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue.first())
print(queue.last())
print('#'*50)
queue.rotate()
print(queue.first())
print(queue.last())



