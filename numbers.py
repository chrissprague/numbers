"""
Personal project written by Christopher Sprague
2/2/14

Performs standard functions on a given list of data
including mean, median, trimmed average, standard variation,
and standard deviation.
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
		self.front = None
	def insert(self, data):
		tmp = self.front
		if tmp == None:
			self.front = Node(data)
		else:
			while ( tmp.next != None ) :
				tmp = tmp.next
			tmp.next = Node(data)
			return 1
			
	def __str__(self):
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
		if self.front == None:
			return 0
		tmp = self.front
		Sum = 0
		while tmp != None:
			Sum += 1
			tmp = tmp.next
		return Sum

	def sort(self): # TODO
		newlist = LinkedList()
		if self.front != None:
			return newlist
		templist = [] # cheating - using Python's sort! Might change this
		tmp = self.front
		while tmp != None:
			templist.append(tmp.data)
			tmp = tmp.next
		templist.sort()
		print(templist)
		for element in templist:
			new_node = Node(element)
			newlist.insert(new_node)
		return newlist

	
def average(data):
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
	if data.front == None:
		return None
	newdata = data.sort()
	print(newdata)
	if data.length() % 2 != 0:
		index = 0
		tmp = data.front
		median_index = data.length() // 2
		print((str)(median_index) + " is the median index")
		while ( index != median_index ) and tmp != None :
			tmp = tmp.next
			index+=1
			print(index)
		return tmp.data
	else:
		index = 0 
		tmp = data.front
		while (index != ( data.length() // 2 ) - 1 ) :
			tmp = tmp.next
			index+=1
		Sum = 0
		Sum += ( ( tmp.data + tmp.next.data ) / 2 )
		return Sum

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



