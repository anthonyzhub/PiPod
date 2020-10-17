class Node:

	def __init__(self, data=None):
		self.next = None
		self.prev = None
		self.data = data
		self.pos = None

	def printInfo(self):

		# OBJECTIVE: Print all informaiton about this node

		print("Node:")
		print("\tPos: ", self.pos)
		print("\tData: ", self.data)
		print("\tAddress: ", self)
		print("\tPrev: ", self.prev)
		print("\tNext: ", self.next)

class LinkList:

	def __init__(self):

		# Create a head and tail node
		self.head = None
		self.tail = None

		# Create counter of list size
		self.size = 0

	def getHead(self):
		return self.head

	def getTail(self):
		return self.tail

	def getMiddleNode(self, headNode):

		# OBJECTIVE: Get middle position of node from link list
		# NOTE: Cannot use self.size because a link list will be divided by half until there is only 1 left,
		# 		so the size will be changing

		# Return node if it is empty
		if headNode == None:
			return headNode

		# Set 2 positions
		slowNode = headNode
		fastNode = headNode

		# Iterate link list
		# Make sure next node and node after that exist
		while (fastNode.next != None) and (fastNode.next.next != None):

			# Update nodes
			slowNode = slowNode.next
			fastNode = fastNode.next.next

		# Return slow_node as middle node
		return slowNode

	def dataAtPosition(self, pos):

		# OBJECTIVE: Return node's data at specific position

		# Exit if pos is out of range
		if pos > self.size or pos <= 0:
			print("Out of range!")
			return 

		# Skip to node at specified position
		currNode = self.getHead()
		for _ in range(pos-1):
			currNode = currNode.next

		# Return data
		return currNode.data

	def isEmpty(self):
		return self.size == 0

	def addHead(self, data):

		# OBJECTIVE: If list is empty, immediately add a head

		# Create a new node
		newNode = Node(data)

		# Update head and tail node
		self.head = newNode
		self.tail = newNode

		# Update size
		self.size += 1
		newNode.pos = self.size

	def addNode(self, data):

		# OBJECTIVE: Add a new node to the end of the list

		# Add head if node is empty
		if self.isEmpty():
			self.addHead(data)
			return

		if self.size == 1:

			# Create a new node
			newNode = Node(data)

			# Update head's pointers
			self.head.next = newNode
			newNode.prev = self.head

			# Update tail node
			self.tail = newNode

			# Update size
			self.size += 1
			newNode.pos = self.size
			
			return

		# Create a new node
		newNode = Node(data)
		self.tail.next = newNode
		newNode.prev = self.tail
		self.tail = newNode

		self.size += 1
		newNode.pos = self.size

	def deleteNode(self, pos):

		# OBJECTIVE: Delete a node from link list

		# Abort if list is empty
		if self.isEmpty():
			return None

		# Get head node
		currNode = self.getHead()

		# Delete node at Nth position
		for _ in range(pos - 1):
			currNode = currNode.next

		# Relink nodes surrounding currNode
		currNode.prev.next = currNode.next
		currNode.next.prev = currNode.prev

		# Delete currNode
		del durrNode

		return True

	def deleteLinkList(self):

		# OBJECTIVE: Delete the entire link list including head and tail nodes

		# Get head node
		currNode = self.head

		while currNode != None:

			# Copy node and go to next node
			oldNode = currNode
			currNode = currNode.next

			# Delete oldNode and decrement size
			del oldNode
			self.size -= 1

		return True

	def sortedMerge(self, linkListA, linkListB):

		# OBJECTIVE: Sort 2 halves of the same link list

		newHead = None

		# Check if either halves of the list are none
		# If data is none, then it must be a tail
		if linkListA == None or linkListA.data == None:
			return linkListB

		if linkListB == None or linkListB.data == None:
			return linkListA

		# Make a recursive call, divide called link list, and come back here
		if linkListA.data <= linkListB.data:
			newHead = linkListA
			newHead.next = self.sortedMerge(linkListA.next, linkListB)
			newHead.next.prev = newHead # Point the next node to newHead
			newHead.prev = None
		else:
			newHead = linkListB
			newHead.next = self.sortedMerge(linkListA, linkListB.next)
			newHead.next.prev = newHead # Point the next node to newHead
			newHead.prev = None

		# Return head sorted link list
		return newHead

	def mergeSort(self, headNode):

		# OBJECTIVE: Sort link list starting with head node

		# Check if link list is empty or by itself
		if (headNode == None) or (headNode.next == None):
			return headNode

		# Get middle node
		middleNode = self.getMiddleNode(headNode)
		nodeAfterMiddle = middleNode.next

		# Set pointer from middleNode to next node as None
		# NOTE: By setting next as none, middle_node would be the end of the link list
		middleNode.next = None

		# Sort left and right side of link list
		leftSide = self.mergeSort(headNode)
		rightSide = self.mergeSort(nodeAfterMiddle)

		# Merge both sides of the link list to one in sorted order.
		# The return value of sortedMerge() is the head node of the new link list
		return self.sortedMerge(leftSide, rightSide)

	def binarySearch(self, leftNode, rightNode, pos):

		# OBJECTIVE: Find data in link list with binary search

		# Exit, if either nodes are none
		if (leftNode == None) or (rightNode == None):
			print("Either nodes are empty")
			exit()

		# Exit, if leftNode and rightNode overlap
		if (leftNode.pos >= rightNode.pos):
			print("Nodes are overlapping")
			return False

		# Get middle node
		middleNode = self.getMiddleNode(leftNode) # Start from the far left
		nodeAfterMiddle = middleNode.next

		middleNode.next = None

		# Check if middleNode is at position
		if middleNode.pos == pos:
			return middleNode.data

		# Go to right half
		elif middleNode.pos > pos:
			return self.binarySearch(leftNode, rightNode.prev, pos)

		# Go to left half
		elif middleNode.pos < pos:
			return self.binarySearch(middleNode.next, rightNode, pos)

	def printForward(self):

		# Get head node
		currNode = self.getHead()

		# Iterate link list
		counter = 1
		while currNode != None:
			print("{}. {}".format(counter, currNode.data))
			currNode = currNode.next
			counter += 1

	def printBackwards(self):

		# Get head node
		currNode = self.getTail()

		# Iterate link list
		counter = 1
		while currNode != None:
			print("{}. {}".format(counter, currNode.data))
			currNode = currNode.prev
			counter += 1

	def printLinkListData(self):

		# OBJECTIVE: Print data of each node inside link list

		# Get head
		currNode = self.getHead()

		while currNode != None:
			currNode.printInfo()
			currNode = currNode.next
