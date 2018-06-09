print """
	The animal at 1 is the first animal of 0th position, bear
	The 1st animal is at 0

	The 3rd animal is the animal at 2, peacock
	The animal at 2 is the 3rd animal

	The 1st animal is at 0, bear
	The animal at 0 is the 1st animal

	The animal at 3 is the 4th animal, kangaroo
	The 4th animal is at 3

	The 5th animal is the animal at 4, whale
	The animal at 4 is the 5th animal

	The animal at 2 is the 3rd animal, peacock
	The 3rd animal is at 2

	The 6th animal is the animal 5, platypus
	The animal at 5 is the 6th animal

	The animal at 4 is the 5th animal, whale
	The 5th animal is the animal at 4
"""

animal = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

num = 0

for i in animal:
	print  "the animal at %d is %s" % (num, animal[num])
	num = num + 1