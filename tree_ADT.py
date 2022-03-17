from linked_list_stack_queue import LinkedQueue 

#------------------------------/ Abstract General Tree /------------------------------------------------------

class Tree:
	"""Abstract base class representing a tree structure."""

	#------------------------------- nested Position class -------------------------------
	class Position:

		def element(self):
			raise NotImplementedError("must be implemented by subclass")


		def __eq__(self, other):
			raise NotImplementedError("must be implemented by subclass")


		def __ne__(self, other):
			return not(self == other)

	#---------- abstract methods that concrete subclass must support ---------------------
	def root(self):
		"""Return Position representing the tree's root (or None if empty)."""
		raise NotImplementedError("must be implemented by subclass")


	def parent(self, p):
		"""Return Position representing p's parent (or None if p is root)."""
		raise NotImplementedError("must be implemented by subclass")


	def num_children(self, p):
		"""Return the number of children that Position p has."""
		raise NotImplementedError("must be implemented by subclass")


	def children(self, p):
		"""Generate an iteration of Positions representing p's children."""
		raise NotImplementedError("must be implemented by subclass")


	def __len__(self):
		"""Return the total number of elements in the tree."""
		raise NotImplementedError("must be implemented by subclass")

	#---------- concrete methods implemented in this class -------------------------------
	def is_root(self, p):
		return self.root() == p


	def is_leaf(self, p):
		return self.num_children(p) == 0


	def is_empty(self):
		return len(self) == 0


	def depth(self, p):
		"""Return the number of levels separating Position p from the root."""

		if self.is_root(p):
			return 0
		else:
			return 1 + self.depth(self.parent(p))


	def height(self, p=None):
		"""Return the height of the subtree rooted at Position p
		If p is None, return the height of the entire tree.
		"""
		if p is None:
			p = self.root()

		elif self.is_leaf(p):
			return 0 
		else:
			return 1 + max(self.height(c) for c in self.children(p))


	def preorder(self):
		"""Generate a preorder iteration of positions in the tree.(O(n + m)T)"""
		if not self.is_empty():
			for p in self._subtree_preoder(self.root()):
				yield p


	def _subtree_preoder(self, p):
		"""Generate a preorder iteration of positions in subtree rooted at p."""

		yield p 							   #visit p before its subtrees
		for c in self.children(p):				   # for each child c	
			for other in self._subtree_preoder(c):  # do preorder of c’s subtree
				yield other                    # yielding each to our caller


	def postorder(self):
		"""Generate a postorder iteration of positions in the tree."""
		if not self.is_empty():
			for p in self._subtree_postorder(self.root()):
				yield p


	def _subtree_postorder(self, p):
		"""Generate a postorder iteration of positions in subtree rooted at p."""

		for c in self.children(p):						# for each child c
			for other in self._subtree_postorder(c):	# do postorder of c’s subtree
				yield other								# yielding each to our caller
		yield p 										# visit p after its subtrees





	def positions(self):
		"""Generate an iteration of all positions of tree T"""
		return self.postorder()


	def __iter__(self):
		"""Generate an iteration of the tree s elements."""
		for p in self.positions():
			yield p.element()


	def Breadth_first(self):
		"""Generate a breadth-first iteration of the positions of the tree(O(n)T)."""
		if not self.is_empty():
			queue = LinkedQueue()          # known positions not yet yielded
			queue.enqueue(self.root())     # starting with the root

			while not queue.is_empty():
				p = queue.dequeue()        # remove from front of the queue
				yield p                    # report this position

				for c in self.children(p):
					queue.enqueue(c)       # add(of p) children to back of queue





#------------------------------/ Abstract Binary Tree /------------------------------------------------------

class BinaryTree(Tree):
	"""Abstract base class representing a binary tree structure"""

	#--------------------- additional abstract methods ---------------------
	def left(self,p):
		"""Return a Position representing p's left child.

		Return None if p does not have a left child.
		"""
		raise NotImplementedError("must be implemented by subclass")

	def right(self, p):
		"""Return a Position representing p's right child.

		Return None if p does not have a right child.
		"""
		raise NotImplementedError("must be implemented by subclass")

	# ---------- concrete methods implemented in this class -----------------

	def sibling(self, p):
		"""Return a Position representing p's sibling (or None if no sibling)."""
		parent = self.parent(p)
		if parent is None:
			return None # must be the root

		else:
			if p == self.left(parent):
				return self.right(parent)
			else:
				return self.left(parent)


	def children(self, p):
		"""Generate an iteration of Positions representing p s children."""
		if self.left(p) is not None:
			yield self.left(p)
		if self.right(p) is not None:
			yield self.right(p)


	def inorder(self):
		"""Generate an inorder iteration of positions in the tree."""
		if not self.is_empty():
			for p in self._subtree_inorder(self.root()):
				yield p


	def _subtree_inorder(self, p):
		"""Generate an inorder iteration of positions in subtree rooted at p."""

		if self.left(p) is not None: 			# if left child exists, traverse its subtree
			for other in self._subtree_inorder(self.left(p)):
				yield other

		yield p   # visit p(root) between its subtrees

		if self.right(p) is not None:  # if right child exists, traverse its subtree
			for other in self._subtree_inorder(self.right(p)):
				yield other


	#  override inherited version to make inorder the default
	def positions(self):
		return self.inorder()



#--------------------Binary Tree simple implemention-----------------
# class Node:
# 	def __init__(self, data):
# 		self.left = None
# 		self.right = None
# 		self.val = data


# root = Node(1)

# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)

# print(root.val)
# print(root.left.val)
# print(root.right.val)
# print(root.left.left.val)

#-------------------- Tree Traversal Algorithms Simple Implemention-----------------
# A function to do preorder tree traversal
# def preorder(root):
 
#     if root:
 
#         # First print the data of node
#         print(root.val),
 
#         # Then recur on left child
#         preorder(root.left)
 
#         # Finally recur on right child
#         preorder(root.right)

# A function to do postorder tree traversal
# def postorder(root):

# 	if root:

# 		# First recur on left child
# 		postorder(root.left)

# 		# Then recur on right child
# 		postorder(root.right)

# 		# finally print the data of node
# 		print(root.val)


# A function to do inorder tree traversal
# def printInorder(root):
 
#     if root:
 
#         # First recur on left child
#         printInorder(root.left)
 
#         # then print the data of node
#         print(root.val),
 
#         # now recur on right child
#         printInorder(root.right)


# A function to do breadth-first tree traversal
# def breadthfirst(root):

   
#     if root is None:
#         return
 
#     # Create an empty queue
#     # for level order traversal
#     queue = []
 
#     # Enqueue Root and initialize height
#     queue.append(root)
 
#     while(len(queue) > 0):
 
#         # Print front of queue and
#         # remove it from queue
#         print(queue[0].data)
#         node = queue.pop(0)
 
#         # Enqueue left child
#         if node.left is not None:
#             queue.append(node.left)
 
#         # Enqueue right child
#         if node.right is not None:
#             queue.append(node.right)
# ------------------------------------------------------------------




class LinkedBinaryTree(BinaryTree):
	"""Linked representation of a binary tree structure."""


    #-------------------------- utility classes --------------------------
	class _Node:

		__slots__ = '_element', '_parent', '_left', '_right'
		def __init__(self, element, parent=None, left=None, right=None):
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right


	class Position(BinaryTree.Position):

		def __init__(self, container, node):
			self._container = container
			self._node = node


		def element(self):
			return self._node._element


		def __eq__(self, other):
			"""Return True if other is a Position representing the same location."""
			return type(other) is type(self) and other._node == self._node

	#-------------------------- utility methods --------------------------
	def _validate(self, p):
		"""Return associated node, if position is valid"""

		if not isinstance(p, self.Position):
			raise TypeError("p must be a valid Position Type")
		if p._container is not self:
			raise ValueError(' p does not belog to this container')
		if p._node._parent is p._node:
			raise ValueError("p is no longer valid")

		return p._node


	def _make_position(self, node):
		"""Return Position instance for given node (or None if no node)."""
		return self.Position(self, node) if node is not None else None
	
	#-------------------------- binary tree constructor --------------------------
	def __init__(self):
		self._root = None
		self._size = 0

	#-------------------------- public accessors ----------------------------------

	def __len__(self):
		return self._size


	def root(self):
		"""Return the root Position of the tree (or None if tree is empty)."""
		return self._make_position(self._root)


	def parent(self, p):
		"""Return the Position of p s parent (or None if p is root)."""
		node = self._validate(p)
		return self._make_position(node._parent)


	def left(self, p):
		"""Return the Position of p's left child (or None if no left child)."""
		node = self._validate(p)
		return self._make_position(node._left)


	def right(self, p):
		"""Return the Position of p's right child (or None if no right child)."""
		node = self._validate(p)
		return self._make_position(node._right)


	def num_children(self, p):
		"""Return the number of children of Position p."""
		node = self._validate(p)
		count = 0
		if node._left is not None:
			count += 1
		if node._right is not None:
			count += 1

		return count


	def _add_root(self, e):
		"""Place element e at the root of an empty tree and return new Position.

		Raise ValueError if tree nonempty.
		"""
		if self._root is not None: 
			raise ValueError("Root exists")
		self._size = 1
		self._root = self._Node(e)
		return self._make_position(self._root)


	def _add_left(self, p, e):
		"""Create a new left child for Position p, storing element e.

		Return the Position of new node.
		Raise ValueError if Position p is invalid or p already has a left child.
		"""
		node = self._validate(p)
		if node._left is not None:
			raise ValueError("Left Child exists")
		self._size += 1
		node._left = self._Node(e, node) # node is its parent
		return self._make_position(node._left)


	def _add_right(self, p, e):
		"""Create a new right child for Position p, storing element e.

		Return the Position of new node.
		Raise ValueError if Position p is invalid or p already has a right child.
		 """
		node = self._validate(p)
		if node._right is not None:
			raise ValueError("Right Child exists")
		self._size += 1
		node._right = self._Node(e, node) # node is its parent
		return self._make_position(node._right)


	def _replace(self, p, e):
		"""Replace the element at position p with e, and return old element."""
		node = self._validate(p)
		old = node._element
		node._element = e
		return old


	def _delete(self, p):
		"""Delete the node at Position p, and replace it with its child, if any.

		Return the element that had been stored at Position p.
		Raise ValueError if Position p is invalid or p has two children.
		"""
		node = self._validate(p)
		if self.num_children(p) == 2:
			raise ValueError("p has two children")

		child = node._left if node._left else node._right # might be None
		if child is not None:
			child._parent = node._parent # child s grandparent becomes parent
		if node is self._root:
			self._root = child
		else:
			parent = node._parent
			if node is parent._left:
				parent._left = child
			else:
				parent._right = child

		self._size -= 1
		node._parent = parent # convention for deprecated node
		return node._element


	def _attach(self, p, t1, t2):
		"""Attach trees t1 and t2 as left and right subtrees of external p."""
		node = self._validate(p)
		if not self.is_leaf(p):
			raise ValueError("Position must be leaf")
		if not type(self) is type(t1) is type(t2):
			raise TypeError("Tree types must match")

		self._size += len(t1) + len(t2)

		if not t1.is_empty():
			t1.root._parent = node
			node._left = t1._root
			t1._root = None
			t1._size = 0
		if not t2.is_empty():
			t2._root._parent = node
			node._right = t2._root
			t2._root = None
			t2._size = 0







# root = tree._add_root(1)

# left_root = tree._add_left(root, 2)
# right_root = tree._add_right(root, 3)

# left_root_left_child = tree._add_left(left_root, 4)
# left_root_right_child = tree._add_right(left_root, 5)

# right_root_left_child = tree._add_left(right_root, 6)
# right_root_right_child = tree._add_right(right_root, 7)


# for e in tree.Breadth_first():
# 	print(e.element())

# tree._delete(right_root_left_child)

# print("#"*50)
# print(len(tree))


# for e in tree.Breadth_first():
# 	print(e.element())

