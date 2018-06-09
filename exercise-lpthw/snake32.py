the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

for i in change:
	print "I got %r" % i

elements = []

# range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understands
	elements.append(i)
	print "Element was: %d" % i

print elements.pop(0)
print elements[1:3]
elements[3] = "apple"
print elements
del elements[2]
print elements
print len(elements)
print elements[2]
