class Node:

	def __init__(self, data="0"):
		self.next = None
		self.prev = None
		self.data = data

	def printInfo(self):

		# OBJECTIVE: Print all informaiton about this node
		print("Node:\n\tData: {}\n\tAddress: {}\n\tPrev: {}\n\tNext: {}".format(self.data, self, self.prev, self.next))

	def printDataOnly(self):

		# OBJECTIVE: Only print the node's data
		print("Node:\n\tData: {}".format(self.data))

class LinkList:

	def __init__(self):

		# Create a head and tail node
		self.head = Node()
		self.tail = Node()

		# Create counter of list size
		self.size = 0

	def isEmpty(self):

		# OBJECTIVE: Check if link list is empty

		return self.size == 0

	def addHead(self, data):

		# OBJECTIVE: If list is empty, immediately add a head

		# Create a new node
		newHead = Node(data)

		# Update head and tail node
		self.head = newHead
		self.tail = newHead

		print("Adding head node")
		self.head.printInfo()
		self.tail.printInfo()

		# Update counter
		self.size += 1

	def addNode(self, data):

		# OBJECTIVE: Add a new node to the end of the list

		# Check if link list is empty
		if self.isEmpty():
			self.addHead(data)
			return None

		# Get head node
		currNode = self.head
		while currNode.next != None:
			currNode = currNode.next

		# Create a new node
		newNode = Node(data)
		newNode.prev = currNode
		currNode.next = newNode

		self.tail = newNode

		# Update counter
		self.size += 1

	def deleteNode(self, pos):

		# OBJECTIVE: Delete a node from link list

		# Abort if list is empty
		if self.isEmpty():
			return None

		# Get head node
		currNode = self.head

		# Delete node at Nth position
		for _ in range(pos - 1):
			currNode = currNode.next

		# Relink nodes surrounding currNode
		currNode.prev.next = currNode.next
		currNode.next.prev = currNode.prev

		# Delete currNode
		del durrNode

		return True
		

	def getHead(self):

		# OBJECTIVE: Return memory address of head node

		return self.head

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

	def sortedMerge(self, linkListA, linkListB):

		# OBJECTIVE: Sort 2 halves of the same link list

		newHead = None

		# Check if either halves of the list are none
		if linkListA == None:
			return linkListB

		if linkListB == None:
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
		node_after_middle = middleNode.next

		# Set pointer from middle_node to next node as None
		# NOTE: By setting next as none, middle_node would be the end of the link list
		middleNode.next = None

		# Sort left and right side of link list
		leftSide = self.mergeSort(headNode)
		rightSide = self.mergeSort(node_after_middle)

		# Merge both sides of the link list to one in sorted order.
		# The return value of sortedMerge() is the head node of the new link list
		return self.sortedMerge(leftSide, rightSide)

	def printLinkList(self):

		# OBJECTIVE: Print all nodes inside link list
		
		# Stop if link list is emtpy
		if self.size <= 0:
			print("Link list is emtpy")
			return None

		# Print link list in normal order
		# Get head node
		currNode = self.head

		# Iterate link list with counter
		counter = 1
		
		print()
		while currNode != None:
			# currNode.printInfo() # NOTE: <= For debugging purposes
			print("{}. {}".format(counter, currNode.data)) # NOTE: <= For commercial use

			currNode = currNode.next
			counter += 1
		print()

	def dataAtPosition(self, pos):

		# OBJECTIVE: Return node's data at specific position

		# Exit if pos is out of range
		if pos > self.size or pos <= 0:
			print("Out of range!")
			return 

		# Skip to node at specified position
		currNode = self.head
		for _ in range(pos-1):
			currNode = currNode.next

		# Return data
		return currNode.data