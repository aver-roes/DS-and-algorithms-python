from positional_listADT import PositionalList



class FavoritesList:
	"""List of elements ordered from most frequently accessed to least."""

	#------------------------------ nested Item class ------------------------------
	class _Item:
		__slots__ = '_value', '_count'

		def __init__(self, e):
			self._value = e # the user's element
			self._count = 0 #  access count initially zero

	#------------------------------- nonpublic utilities -------------------------------
	def _find_position(self, e):
		"""Search for element e and return its Position (or None if not found)."""

		walk = self._data.first()
		while walk is not None and walk.element()._value != e:
			walk = self._data.after(walk)
		return walk


	def _move_up(self, p):
		"""Move item at Position p earlier in the list based on access count."""

		if p != self._data.first(): # as long as is not the 1st element consider moving...
			cnt = p.element()._count
			walk = self._data.before(p)

			if cnt > walk.element()._count: # must shift forward
				while(walk != self._data.first() and cnt > self._data.before(walk).element()._count):
					walk = self._data.before(walk)
				self._data.add_before(walk, self._data.delete(p)) # delete/reinsert

	#------------------------------- public methods -------------------------------
	def __init__(self):
		"""Create an empty list of favorites."""
		self._data = PositionalList() # will be a list of _item instance


	def __len__(self):
		return len(self._data)


	def is_empty(self):
		return len(self._data) == 0


	def access(self, e):
		"""Access element e, thereby increasing its access count."""
		p = self._find_position(e) # try to locate existing element
		if p is None:
		    p = self._data.add_last(self._Item(e)) # if new, place at last

		p.element()._count += 1 # always increment count
		self._move_up(p) # consider moving forward


	def remove(self, e):
		"""Remove element e from the list of favorites."""
		p  = self._find_position(e)
		if p is not None:
		   self._data.delete(p) #  delete, if found


	def top(self, k):
		"""Generate sequence of top k elements in terms of access count."""
		if not 1 <= k <= len(self):
			raise ValueError("Illegal value for k")

		walk = self._data.first()
		for j in range(k):
			item = walk.element()
			yield item._value
			walk = self._data.after(walk)




F = FavoritesList()



class FavoritesListMTF(FavoritesList):
	"""list of elements ordered with move-to-front heuristic"""

	def _move_up(self, p):
		if p != self._data.first():
			self._data.add_first(self._data.delete(p))

	def top(self, k):
		if not 1<=k<=len(self):
			raise ValueError('Illegal value for k')

		temp = PoisitionalList()
		for item in self._data:
			temp.add_last(item)

		for j in range(k):
			highPos = temp.first()
			walk = temp.after(highPos)
			while walk is not None:
				if walk.element()._count > highPos.element()._count:
					highPos = walk
				walk = temp.after(walk)
			yield highPos.element()._value
			temp.delete(highPos)



