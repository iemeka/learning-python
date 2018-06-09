def loops(i, six, increaseBy):
	numbers = []

	while i < six:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + increaseBy
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

		print "The numbers: "

	for num in numbers:
		print num

loops(0, 6, 1)



def loops2():
	numbers = []
	for i in range(0, 6):
		print "At the top i is %d" % i
		numbers.append(i)
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

		print "The numbers: "

	print numbers

loops2()
