"""
Personal project written by Christopher Sprague
2/2/14

Performs standard functions on a given list of data
including mean, median, trimmed average, standard variation,
and standard deviation.

File: numbers.py
Revisions: see git commits.

"""

class Node:
	"""
	node class as part of the linked list structure
	
	contains floats representing one piece of 
	data in our list
	"""
	__slots__=("data", "next")
	def __init__(self, data):
		self.data = data
		self.next = None
	def __str__(self):
		return self.data
	

class LinkedList:
	"""
	Linked list structure, made up of nodes,
	which represents the data set which the
	mathematical functions and operations rely on.
	"""
	__slots__=("front")
	def __init__(self):
		'''
		initialize a LinkedList object
		'''
		self.front = None
	def insert(self, data):
		"""
		insert method for a LinkedList - 
		to use:
			my_linked_list.insert(####)
		to insert a number into this instance
		of a LinkedList.
		"""
		tmp = self.front
		if tmp == None:
			self.front = Node(data)
		else:
			while ( tmp.next != None ) :
				tmp = tmp.next
			tmp.next = Node(data)
			return 1
			
	def __str__(self):
		"""
		string representation of a LinkedList
		instance. Used primarily for printing
		and casting a LinkedList to a string.
		"""
		tmp = self.front
		string = "["
		while tmp != None:
			if tmp.data != None:
				string += (str)(tmp.data)
				if tmp.next != None:
					string += ", "
				tmp = tmp.next
		return string + "]"
	def length(self):
		"""
		calculates and returns the length
		of the given list.
		returns an integer.
		"""
		if self.front == None:
			return 0
		tmp = self.front
		Sum = 0
		while tmp != None:
			Sum += 1
			tmp = tmp.next
		return Sum

	def sort(self):
		"""
		sorts the list by returning 
		an instance of a LinkedList containing
		the same data that the given list contained,
		but min-sorted traditionally (i.e. 1<2)
		"""
		if self.front == None:
			return newlist
		newlist = LinkedList()
		tmp = self.front
		while self.front != None :
			minimum = self.front.data
			tmp = self.front
			while tmp != None:
				if tmp.data < minimum : 
					minimum = tmp.data
				tmp = tmp.next
			tmp2 = self.front
			if tmp2.data == minimum :
				newlist.insert(minimum)
				self.front = self.front.next
			else:
				while tmp2.next != None :
					if tmp2.next.data == minimum : 
						newlist.insert(minimum)
						tmp2.next = tmp2.next.next
						break
					tmp2 = tmp2.next # yolo
		return newlist

	
def average(data):
	"""
	calculates the average of the data
	given in the argument "data".
	"""
	if data.front == None :
		return None
	tmp = data.front
	Sum = 0
	while tmp != None:
		Sum += tmp.data
		tmp = tmp.next
	try:
		return Sum/data.length()
	except ZeroDivisionError:
		return 0
	
def median(data):
	"""
	calculate the median value of the data
	given in arg, "data".
	Relies on sorting the data - see
	LinkedList's internal sort function.
	"""
	if data.front == None:
		return None
	newlist = data.sort()
	if newlist.length() % 2 != 0:
		index = 0
		tmp = newlist.front
		median_index = newlist.length() // 2
		while ( index != median_index ) and tmp != None :
			tmp = tmp.next
			index+=1
		return tmp.data
	else:
		index = 0 
		tmp = newlist.front
		while (index != ( newlist.length() // 2 ) - 1 ) :
			tmp = tmp.next
			index+=1
		Sum = 0
		Sum += ( ( tmp.data + tmp.next.data ) / 2 )
		return Sum

def stdDev(data,average=None):
	"""
	calculate the standard deviation of
	a data set, while making use of an
	already-supplied average value
	(to avoid having to call the average function again)
	default/unprovided value forcibly calls average
	if it is not provided.
	"""
	if average == None : 
		average = average(data)
	if data.length() == 0 : # no data = no std dev
		return None
	
	pass

def main():
	"""
	main function - covers the important
	functionality of the program
	"""
	
	text = "temp"
	theList = LinkedList()
	first_prompt = True
	while ( text.strip() != " " and text.strip() != "" and text.strip() != "done" ) :
		if first_prompt:
			print("Enter numbers to be put into the data set (done to quit):")
			first_prompt = False
		try:
			value = (input("> "))
		except EOFError:
			print()
			break
		if value in ["", " ", "done", "quit"]: # done taking input
			break
		try:
			value = (float)(value)
			theList.insert(value)
		except ValueError:
			print("Error: Non-numerical input")
		
		
	print(theList)
	print("Mean: " + (str)(average(theList)))
	print("Median: " + (str)(median(theList)))

	






main()



