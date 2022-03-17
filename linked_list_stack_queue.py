#---------------------Simple implementation of Linked list---------------------------


# Linked list implementation in Python


# class Node:
#     # Creating a node
#     def __init__(self, item):
#         self.item = item
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None


# if __name__ == '__main__':

#     linked_list = LinkedList()

#     # Assign item values
#     linked_list.head = Node(1)
#     second = Node(2)
#     third = Node(3)

#     # Connect nodes
#     linked_list.head.next = second
#     second.next = third

#     # Print the linked list item
#     while linked_list.head != None:
#         print(linked_list.head.item, end=" ")
#         linked_list.head = linked_list.head.next

#---------------------------------------------------------------------









class Empty(Exception):
	pass


class LinkedStack:

################################/nested _Node class/################################
	class _Node:
		""" Lightweight, nonpublic class for storing a singly linked node """
		__slots__ = '_element', '_next' #streamline memory usage

		def __init__(self, element, next):
			self._element = element
			self._next = next
################################/stack methods/################################
	def __init__(self):
		self._head = None
		self._size = 0


	def __len__(self):

		return self._size


	def is_empty(self):
		return self._size == 0


	def push(self, e):
		""" Add element e to the top of the stack aka: add an elememt at the head of the Linked_List""" 
		self._head = self._Node(e, self._head)
		self._size += 1
		return e


	def top(self):	

		if self.is_empty():
			raise Empty('Stack is Empty')
		return self._head._element


	def reverse(self):
		""" reverse the (linkedlist) stack"""
		current = self._head
		prev = None
		while(current != None):
			next = current._next
			current._next = prev
			prev = current
			current = next
		self._head = prev
		return self._head



	def pop(self):
		""" Remove and return the element from the top of the stack (i.e., LIFO).
			aka: remove the head of the Linked-List""" 
		if self.is_empty():
			raise Empty('Stack is Empty')

		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		return answer




# stack = LinkedStack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
# print("#"*50)
# stack.reverse()
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())


# reverse stack using another stack
# stack = LinkedStack()

# print(stack.push(1))
# print(stack.push(2))
# print(stack.push(3))
# print("#"*50)

# stackreverse = LinkedStack()


# for i in range(len(stack)):
# 	print(stackreverse.push(stack.pop()))






class LinkedQueue:

	class _Node:
		""" Lightweight, nonpublic class for storing a singly linked node """
		__slots__ = '_element', '_next' #streamline memory usage

		def __init__(self, element, next):
			self._element = element
			self._next = next


	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0


	def __len__(self):

		return self._size


	def is_empty(self):

		return self._size == 0


	def first(self):

		if self.is_empty():
			raise Empty('Queue is Empty')

		return self._head._element


	def enqueue(self, e):

		newest = self._Node(e, None)
		if self.is_empty():
			self._head = newest
		else:
			self._tail._next = newest

		self._tail = newest
		self._size += 1


	def dequeue(self):

		if self.is_empty():
			raise Empty('Queue is Empty')

		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		if self.is_empty():
			self._tail = None
		return answer


# queue = LinkedQueue()

# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(7)
# print(queue.first())
# queue.dequeue()
# print(queue.first())
# print(len(queue))