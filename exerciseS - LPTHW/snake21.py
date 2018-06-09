def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)

# print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)


# print "Here is a puxxle."

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print "That becomes: ", what, "can you do it by hand?"


#10 + 360 / 15 * 12 - 33

mult = multiply(10, 12)
div = divide(360, mult)
add = add(10 ,div)


solve = subtract(add, 33)

print solve
