from positional_listADT import Empty


class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    #------------------------------ nested _Item class ------------------------------
    class _Item:
      """Lightweight composite to store priority queue items."""
      __slots__ = '_key', '_value'

      def __init__(self, k, v):
        self._key = k
        self._value = v

      def __lt__(self, other):
        return self._key < other._key    # compare items based on their keys

      def __repr__(self):
        return '({0},{1})'.format(self._key, self._value)

  #------------------------------ public behaviors ------------------------------
    def is_empty(self):                  # concrete method assuming abstract len
      """Return True if the priority queue is empty."""
      return len(self) == 0


#------------------------------- Heap Priority Queue -----------------------------
class HeapPriorityQueue(PriorityQueueBase):
  """A min-oriented priority queue implemented with a binary heap."""
  #------------------------------ Non-public behaviors ---------------------------
  def _parent(self, j):
    return (j - 1) // 2


  def _left(self, j):
    return 2*j + 1


  def _right(self, j):
    return 2*j + 2

  def _has_left(self, j):
    return self._left(j) < len(self._data) #  index beyond end of list?


  def _has_right(self, j):
    return self._right(j) < len(self._data)


  def _swap(self, i, j):
    """Swap the elements at indices i and j of array."""
    self._data[i], self._data[j] = self._data[j], self._data[i]


  def _upheap(self, j):
    """Up-heap bubbling"""
    parent = self._parent(j)
    if j > 0 and self._data[j] < self._data[parent]:
      self._swap(j, parent)
      self._upheap(parent) # recur at position of parent


  def _downheap(self, j):
    """ Down-heap bubbling"""
    if self._has_left(j):
      left = self._left(j)
      small_child = left

      if self._has_right(j):
        right = self._right(j)
        if self._data[right] < self._data[left]:
          small_child = right

      if self._data[small_child] < self._data[j]:
        self._swap(j , small_child)
        self._downheap(small_child)


  #------------------------------ Public behaviors -------------------------------

  def __init__(self):
    self._data = []


  def __len__(self):
    return len(self._data)


  def add(self, key, value):
    """Add a key-value pair to the priority queue."""
    self._data.append(self._Item(key, value))
    self._upheap(len(self._data) - 1) # upheap newly added position


  def min(self):
    """Return but not remove (k,v) tuple with minimum key."""
    if self.is_empty():
      raise Empty("Priority queue is empty.")

    item = self._data[0]
    return (item._key, item._value)


  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key."""
    if self.is_empty():
      raise Empty("Priority queue is empty.")

    self._swap(0, len(self._data) - 1)
    item = self._data.pop()
    self._downheap(0)
    return (item._key, item._value)




heap = HeapPriorityQueue()

heap.add(5,'A')
heap.add(9,'C')
heap.add(3,'B')
heap.add(7,'D')
print(heap.min())
print(len(heap))
print(heap.remove_min())
print(heap.remove_min())
print(heap.remove_min())
print(heap.remove_min())
print(heap.is_empty())

