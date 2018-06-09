#validate base-word
def check(a):
	print "Type an eight letter word"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	if len(a) != 8:
		print "\n Not up to eight letters \n"
		return check(raw_input(': '))
	return a

def eight(num):
	return num

# Analyse and compare.**level one**
def typeFirst_mid():
	print "Type a word that begins with the fourth letter"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	first_mid = raw_input(": ")
	if first_mid[0] == base_word[3]:
		print "passed! onto the next one"
		typeSecond_mid()
	else:
		return typeFirst_mid()

def typeSecond_mid():
	print "Type a word that begins with fifth letter"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	second_mid = raw_input(": ")
	if second_mid[0] == base_word[4]:
		print "congratulations! Next level"
		typeLast_first()
	else:
		return typeSecond_mid()

def typeLast_first():
	print "Type a word that contains both the fourth and last letter"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	A_word = raw_input(": ")
	if  (base_word[7], base_word[0] in A_word):
		print "contained!! continue"
		typeSecond_seventh()
	else:
		return typeLast_first()

def typeSecond_seventh():
	print "Type a word tha contains both second and seventh letter"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	the_word = raw_input(": ")
	if (base_word[1], base_word[6] in the_word):
		print "first level completed"
		level2()
	else:
		return typeSecond_seventh()

def level2():
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	print """

	Welcome to level 2 !!!

	"""





base_word = eight(check(raw_input(": ")))
typeFirst_mid()
