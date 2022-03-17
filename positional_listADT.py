###############/Implementing Positional List using Doubly LinkedList as base/###############


class Empty(Exception):
	pass



class _DoublyLinkedListBase:
	"""A base class providing a doubly linked list representation."""


	class _Node:
		""" Lightweight, nonpublic class for storing a singly linked node """
		__slots__ = '_element', '_prev', '_next' #streamline memory usage

		def __init__(self, element, prev, next):
			self._element = element
			self._prev = prev
			self._next = next


	def __init__(self):
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0


	def __len__(self):

		return self._size


	def is_empty(self):

		return self._size == 0


	def _insert_between(self, e, predecessor, successor):
		"""Add element e between two existing nodes and return new node."""

		newest = self._Node(e, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1

		return newest


	def _delete_node(self, node):
		"""Delete nonsentinel node from the list and return its element."""

		predecessor = node._prev
		successor = node._next
		predecessor._next = successor
		successor._prev = predecessor
		self._size -= 1

		element = node._element
		node._prev = node._next = node._element = None
		return element



class PositionalList(_DoublyLinkedListBase):
	"""A sequential container of elements allowing positional access."""

	#-------------------------- nested Postion class --------------------------
	class Position:
		"""An abstraction representing the location of a single element."""


		def __init__(self, container, node):
			"""Constructor should not be invoked by user."""
			self._container = container
			self._node = node


		def element(self):
			"""Return the element stored at this Position."""
			return self._node._element


		def __eq__(self, other):
			"""Return True if other is a Position representing the same location"""
			return type(other) is type(self) and other._node is self._node


		def __ne__(self, other):
			"""Return True if other does not represent the same location."""
			return not (self == other) # opposite of __eq__

	#-------------------------- utility method --------------------------

	def _validate(self, p):
		"""Return the node at the given position, or raise appropriate error if invalid."""
		if not isinstance(p, self.Position):
			raise TypeError('p Must Be Proper Position Type')

		if p._container is not self:
			raise ValueError('p Does Not Belong To This Container')

		if p._node._next is None:
			raise ValueError('p Is No Longer Valid')

		return p._node


	def _make_position(self, node):
		"""Return Position instance for given node (or None if sentinel)."""

		if node is self._header and node is self._trailer:
			return None # boundary violation
		else:
			return self.Position(self, node) # legitimate position

	#-------------------------- accessors --------------------------

	def first(self):
		""" Return the first Position in the list (or None if list is empty)."""
		return self._make_position(self._header._next)


	def last(self):
		"""Return the last Position in the list (or None if list is empty)."""
		return self._make_position(self._trailer._prev)


	def before(self, p):
		"""Return the Position just before Position p (or None if p is first)."""
		node  = self._validate(p)
		return self._make_position(node._prev)


	def after(self, p):
		"""Return the Position just after Position p (or None if p is last)."""
		node = self._validate(p)
		return self._make_position(node._next)

	
	def __iter__(self):
		"""Generate a forward iteration of the elements of the list."""
		cursor = self.first()
		while cursor is not None:
			try:
				yield cursor.element()
				cursor = self.after(cursor)
			except:
				break


	#-------------------------- mutators --------------------------
	# override inherited version to return Position, rather than Node
	def _insert_between(self, e, predecessor, successor):
		"""Add element between existing nodes and return new Position."""
		node = super()._insert_between(e, predecessor, successor)
		return self._make_position(node)


	def add_first(self, e):
		"""Insert element e at the front of the list and return new Position"""
		return self._insert_between(e, self._header, self._header._next)


	def add_last(self, e):
		"""Insert element e at the back of the list and return new Position."""
		return self._insert_between(e, self._trailer._prev, self._trailer)


	def add_before(self, p, e):
		"""Insert element e into list before Position p and return new Position."""
		original  = self._validate(p)
		return self._insert_between(e, original._prev, original)
	

	def add_after(self, p, e):
		""" Insert element e into list after Position p and return new Position."""
		original = self._validate(p)
		return self._insert_between(e, original, original._next)


	def delete(self, p):
		"""Remove and return the element at Position p"""
		original = self._validate(p)
		return self._delete_node(original)


	def replace(self, p, e):
		"""Replace the element at Position p with e

		   Return the element formerly at Position p.
		"""

		original = self._validate(p)
		old_value = original._element
		original._element = e
		return old_value



L = PositionalList()		

first = L.add_last(9)
second = L.add_last(7)
third = L.add_last(6)
fourth = L.add_last(8)


# before_fourth = L.add_before(fourth,30)
# L.add_after(first, 12)
# L.delete(before_fourth)
# L.replace(first, 89)

# print(L.after(first) == second)
# print(L.after(first) == fourth)



for e in L:
	print(e)

print(len(L))

def insertion_sort(L):
	"""Sort PositionalList of comparable elements into nondecreasing order."""

	if len(L) > 1:
		marker = L.first()
		while marker != L.last():

			pivot = L.after(marker)
			value = pivot.element()

			if value > marker.element():
				marker = pivot
			else:
				walk = marker
				while walk != L.first() and L.before(walk).element() > value:
					walk = L.before(walk)
				L.delete(pivot)
				L.add_before(walk, value)


# print('#'*50)
# insertion_sort(L)
# for k in L:
# 	print(k)




