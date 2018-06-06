people = 30 
cars = 4
buses = 15

if cars > people:
	print "we should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if (buses == cars and buses > cars):
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "we still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."