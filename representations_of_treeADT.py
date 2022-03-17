from tree_ADT import LinkedBinaryTree



def preorder_indent(Tree, position, depth):
	"""Print preorder representation of subtree of Tree rooted at position p at depth d."""
	
	print(2*depth*' ' + position.element()) #  use depth for indentation
	for child in Tree.children(position):
		preorder_indent(Tree, child, depth+1)



def preorder_label(Tree, position, depth, path):
	"""Print labeled representation of subtree of Tree rooted at position p at depth d."""

	label = '.'.join(str(j+1) for j in path)  # displayed labels are one-indexed
	print(2*depth*' '+ label, position.element())
	path.append(0)
	for child in Tree.children(position):
		preorder_label(Tree, child, depth+1, path)
		path[-1] += 1
	path.pop()



def parenthesize(Tree, position):
	"""Print parenthesized representation of subtree of T rooted at position p."""

	print(position.element(), end='') # use of end avoids trailing newline
	if not Tree.is_leaf(position):
		first_time = True
		for child in Tree.children(position):
			sep = '(' if first_time else ','
			print(sep, end='')
			first_time = False # any future passes will not be the first
			parenthesize(Tree,child) # recur on child
		print(')', end='')



tree = LinkedBinaryTree()

root = tree._add_root('Hasson')

left_root = tree._add_left(root, 'Ali')
right_root = tree._add_right(root, 'Omer')

left_root_left_child = tree._add_left(left_root, 'Mariam')
left_root_right_child = tree._add_right(left_root, 'Johnny')

right_root_left_child = tree._add_left(right_root, 'Susan')
right_root_right_child = tree._add_right(right_root, 'Sal')

left_root_right_child_kid = tree._add_left(left_root_right_child,'james')


preorder_indent(tree, root, 0)

# preorder_label(tree, root, 0, path=[])

# parenthesize(tree, root)


def compute_space(Tree, position):
	""" assuming that a space( ) method of each tree element reports the local space used at that
		position.
	"""
	sub_total = position.space()                  # space used at position p
	for child in Tree.children(position):
		sub_total += compute_space(Tree, child)   # add child’s space to subtotal
	return sub_total