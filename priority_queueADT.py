from positional_listADT import PositionalList, Empty

#---------------------------------- simple implementation ----------------------------------

# class Node:
#   def __init__(self, data, priority):
#     self.data = data
#     self.priority = priority


# class PriorityQueue:

#   def __init__(self):
#     self.queue = []


#   def size(self):
#     return len(self.queue)

#   def show(self):
#     for element in self.queue:
#       print(f"{element.data} - {element.priority}")

#   def insert(self, node):
#     if self.size() == 0:
#       self.queue.append(node)
#     else:
#       for i in range(0, self.size()):
#         if node.priority >= self.queue[i].priority:
#           if i == (self.size() -1):
#             self.queue.insert(i+1, node)
#           else:
#             continue
#         else:
#           self.queue.insert(i, node)
#           return True

#   def delete(self):
#     self.queue.pop(0)



# pQueue = PriorityQueue()
# node1 = Node("C", 3)
# node2 = Node("B", 2)
# node3 = Node("A", 1)
# node4 = Node("Z", 26)
# node5 = Node("Y", 25)
# node6 = Node("L", 12)

# pQueue.insert(node1)
# pQueue.insert(node2)
# pQueue.insert(node3)
# pQueue.insert(node4)
# pQueue.insert(node5)
# pQueue.insert(node6)
# pQueue.show()
# print("--------")
# pQueue.delete()
# pQueue.show()


#-----------------------------------------------------------------------------------------------

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

#------------------------------- Unsorted Priority Queue ------------------------

class UnsortedPriorityQueue(PriorityQueueBase): # base class defines _Item
  """A min-oriented priority queue implemented with an unsorted list."""

  #----------------------------- nonpublic behavior -----------------------------
  def _find_min(self):
    """Return Position of item with minimum key."""
    if self.is_empty():               # is_empty inherited from base class
      raise Empty('Priority queue is empty')
    small = self._data.first()
    walk = self._data.after(small)
    while walk is not None:
      if walk.element() < small.element():
        small = walk
      walk = self._data.after(walk)
    return small

  #------------------------------ public behaviors ------------------------------
  def __init__(self):
    """Create a new empty Priority Queue."""
    self._data = PositionalList()

  def __len__(self):
    """Return the number of items in the priority queue."""
    return len(self._data)

  def add(self, key, value):
    """Add a key-value pair."""
    self._data.add_last(self._Item(key, value))

  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.
    Raise Empty exception if empty.
    """
    position = self._find_min()
    item = position.element()
    return (item._key, item._value)

  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.
    Raise Empty exception if empty.
    """
    position = self._find_min()
    item = self._data.delete(position)
    return (item._key, item._value)





# P = UnsortedPriorityQueue()

# P.add(5,'A')
# P.add(9,'C')
# P.add(3,'B')
# P.add(7,'D')
# print(P.min())
# print(P.remove_min())
# print(P.remove_min())
# print(len(P))
# print(P.remove_min())
# print(P.remove_min())
# print(P.is_empty())
# # P.remove_min()



#------------------------------- sorted Priority Queue -----------------------------

class SortedPriorityQueue(PriorityQueueBase):
  """A min-oriented priority queue implemented with a sorted list"""

  def __init__(self):
    self._data = PositionalList()


  def __len__(self):
    return len(self._data)


  def add(self, key, value):

    newest = self._Item(key, value)
    walk = self._data.last()

    while walk is not None and newest < walk.element():
      walk = self._data.before(walk)

    if walk is None:
      self._data.add_first(newest)
    else:
      self._data.add_after(walk, newest)


  def min(self):

    if self.is_empty():
      raise Empty('Priority queue is empty')

    position = self._data.first()
    item = position.element()
    return (item._key, item._value)


  def remove_min(self):

    if self.is_empty():
      raise Empty('Priority queue is empty')

    item = self._data.delete(self._data.first())
    return (item._key, item._value)




P = SortedPriorityQueue()

P.add(5,'A')
P.add(9,'C')
P.add(3,'B')
P.add(7,'D')
print(P.min())
print(P.remove_min())
print(P.remove_min())
print(len(P))
print(P.remove_min())
print(P.remove_min())
print(P.is_empty())
# P.remove_min()

