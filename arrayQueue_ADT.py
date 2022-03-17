
class Empty(Exception):
	pass


	

class ArrayQueue:

	DEFAULT_CAPACITY = 10 

	def __init__(self):
		self._data = [None] * self.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0  # the first element in the queue


	def __len__(self):
		"""Return the number of elements in the queue."""
		return self._size


	def is_empty(self):
		"""Return True if the queue is empty."""
		return self._size == 0


	def first(self):
		""" Return (but do not remove) the element at the front of the queue.

			Raise Empty exception if the queue is empty
		"""
		if self.is_empty():
			raise Empty("Queue is Empty")
		else:
			return self._data[self._front]



	def enqueue(self, e):

		"""Add an element to the back of queue."""

		if self._size == len(self._data):
			self._resize(2 * len(self._data))

		# formula to compute the location of the next opening
		avail = (self._front + self._size) % len(self._data) 
		self._data[avail] = e
		self._size += 1



	def dequeue(self):
		"""Remove and return the first element of the queue (i.e., FIFO).

			Raise Empty exception if the queue is empty.
		 """
		if self.is_empty():
			raise Empty("Queue is Empty")

		answer = self._data[self._front]
		self._data[self._front] = None

		self._front = (self._front + 1) % len(self._data)
		self._size -= 1

		# when  no. of elements in it the queue is below one fourth of its capacity
		# reduce the underling array(self._data) to half of its current size
		if 0 < self._size < len(self._data) // 4:
			self._resize(len(self._data) // 2)

		return answer


	def _resize(self, cap):
		"""Resize to a new list of capacity >= len(self)."""

		old = self._data #  keep track of existing list
		self._data = [None] * cap # allocate list with new capacity

		walk = self._front
		for k in range(self._size): # only consider existing elements

			self._data[k] = old[walk] # intentionally shift indices
			walk = (1 + walk) % len(old)  #  use old size as modulus

		self._front = 0 #  front has been realigned


	def __repr__(self):
		""" A String representaion of the Queue """

		return f"{self._data}"




# q = ArrayQueue()

# q.enqueue(5)
# q.enqueue(10)
# q.enqueue(4)
# q.enqueue(7)
# q.dequeue()
# print(q.first())
# print(q.is_empty())



# print(q)




class ArrayDeque(ArrayQueue):

  def __init__(self):
  	super().__init__()



  def last(self):
    """ Return (but do not remove) the element at the end of the deque.

      Raise Empty exception if the queue is empty
    """
    if self.is_empty():
      raise Empty("Queue is Empty")
    
    return self._data[(self._front + self._size - 1)%len(self._data)]  


  def add_first(self, e):
  	""" Add an element at the front of the deque """

  	if self._size == len(self._data):
  		self._resize(2 * len(self._data))

  	self._front = (self._front -1) % len(self._data)
  	self._data[self._front] = e
  	self._size += 1

    



  def add_last(self, e):
  	"""Add an element at the back of the deque """

  	return self.enqueue(e)




  def delete_first(self):
    """Remove and return the first element of the deque.

       Raise Empty exception if the deque is empty.
     """
    return self.dequeue()


  def delete_last(self):
    """similar to delete first but at end of deque"""

    if self.is_empty():
      raise Empty('Queue is empty')

    back = (self._front + self._size - 1) % len(self._data)
    last_el = self._data[back]
    self._data[back] = None
    self._size -= 1

    if 0 < self._size < len(self._data) // 4:
      self._resize(len(self._data) // 2)

    return last_el





D = ArrayDeque()

D.add_last(4)
D.add_last(5)
D.add_last(6)
D.add_first(3)
D.add_first(2)
D.add_first(1)


print(D)

print(D.first())
print(D.last())
D.add_last(7)
print(D)
print(D.last())
D.delete_first()
print(D)
D.delete_last()
print(D)