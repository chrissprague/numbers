"""

Personal project written and designed by Christopher Sprague
2/2/14

Performs standard functions on a given list of data
including mean, median, trimmed average, standard variation,
and standard deviation.

standard deviation and standard variance
are SAMPLE std dev & std var.

File: numbers.py

Revisions: see git commits.
https://github.com/chrissprague

Author: Christopher Sprague <css7209@rit.edu>

"""

"""
values used in determining trimmed mean - 
because the trimmed mean can be evaluated many ways
and to many different extents
"""
TRIMMED_MEAN_PERCENT = 12.5
TRIMMED_MEAN_NUM_TRIMMED = 1
TRIMMED_MEAN_USE_PERCENT = False
# end global constant definitions

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

def trimmed_mean ( lst ) :
	"""
	calculate the trimmed mean for a set of data
	This instance of trimmed mean will cut off the
	outlying 12.5% of data in attempt to "fix"
	or more accurately portray the data

	the number trimmed using percent is rounded UP
	
	for example - if the number trimmed by % is determined
	to be 3.75 data points off the front/back,
	4 data points will be trimmed from the front/back.
	"""
	if lst.length() == 0 :
		return None
	if TRIMMED_MEAN_USE_PERCENT : # trimmed mean to use % cut-off of data
		num_trimmed = ( lst.length() * TRIMMED_MEAN_PERCENT / 100 )
		num_trimmed = round(num_trimmed)
		# lower/upper bounds determine where to start/stop collecting data
		lower_bound = num_trimmed
		upper_bound = lst.length() - num_trimmed
		count = 0
		tmp = lst.front
		Sum = 0
		while tmp != None :
			if not ( ( count < lower_bound ) or ( count >= upper_bound ) ) :
				Sum += tmp.data
			tmp = tmp.next
			count += 1
		return (Sum / (lst.length() - 2*num_trimmed) )
	else : # use a discrete number of data points to trim finding average
	# this is exactly like percent-based trimmed mean, but this method
	# cuts out the middle man, so to speak, by simply providing
	# the number of data points we want cut off.
		num_trimmed = round(TRIMMED_MEAN_NUM_TRIMMED)
		lower_bound = num_trimmed
		upper_bound = lst.length() - num_trimmed
		count = 0
		tmp = lst.front
		Sum = 0
		while tmp != None : 
			if not ((count<lower_bound)or(count>=upper_bound)):
				Sum += tmp.data
			tmp = tmp.next
			count+=1
		return (Sum/(lst.length()-2*num_trimmed))
		
	return None



def median(data):
	"""
	calculate the median value of the data
	given in arg, "data".
	Relies on sorting the data - see
	LinkedList's internal sort function.
	"""
	if data.front == None:
		return None
	newlist = data
	# newlist = data.sort() # no longer necessary, and discouraged from sorting here
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

def stdVariance(lst,avg):
	"""
	calculate standard variance of the data
	set making use of a given average value.
	"""
	if avg == None :
		avg = average ( lst )
	if lst.length() == 0 : # no data = no std variance
		print("yo")
		return None
	tmp = lst.front
	stdvar = 0
	while tmp != None : 
		stdvar += (tmp.data - avg)*(tmp.data - avg) # basically squared
		tmp = tmp.next
	stdvar = (stdvar)/(lst.length())
	return stdvar



def stdDev(std_var):
	"""
	calculate the standard deviation of
	a data set, while making use of an
	already-supplied standard variance value ONLY
	"""
	return ((std_var)**(0.5)) # square root of standard variance

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
			print("Enter numbers to be put into the data set ('done' to quit):")
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
	sorted_list = theList.sort()
	avg = average(sorted_list)
	std_var = stdVariance(sorted_list,avg)
	std_dev = stdDev(std_var)
	tm = (str)(trimmed_mean(sorted_list))
	print("Mean: " + (str)(avg))
	print("Median: " + (str)(median(sorted_list)))
	print("Standard Variance: " + (str)(std_var))
	print("Standard Deviation: " + (str)(std_dev))
	if TRIMMED_MEAN_USE_PERCENT : 
		print("Trimmed Mean ("+(str)(TRIMMED_MEAN_PERCENT)+"%): " + tm)
	else:
		print("Trimmed Mean (num="+(str)(TRIMMED_MEAN_NUM_TRIMMED)+"): " + tm)





main()



