#validate base-word
def check(a):
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	if len(a) != 8:
		print "\n Not up to eight letters \n"
		return check(raw_input(': '))
	return a

def eight(num):
	return num

# Analyse and compare.**level one**
def typeFirst_mid():
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	first_mid = raw_input("Type a word that begins with the fourth letter: ")
	if first_mid[0] == base_word[3]:
		print "passed! onto the next one"
		typeSecond_mid()
	else:
		print "incorrect!"
		return typeFirst_mid()
	return first_mid

def typeSecond_mid():
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	second_mid = raw_input("Type a word that begins with fifth letter: ")
	if second_mid[0] == base_word[4]:
		print "congratulations! Next level"
		typeLast_first()
	else:
		print "incorrect!"
		return typeSecond_mid()
	return second_mid

def typeLast_first():
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	A_word = raw_input("Type a word that contains both first and last letter: ")
	if  (base_word[7] in A_word) and (base_word[0] in A_word):
		print "contained!! continue"
		typeSecond_seventh()
	else:
		return typeLast_first()
	return A_word

def typeSecond_seventh():
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	the_word = raw_input("Type a word that contains both second and seventh letter: ")
	if (base_word[1] in the_word) and (base_word[6] in the_word):
		print "first level completed"
		level2()
	else:
		print "incorrect!"
		return typeSecond_seventh()
	return the_word

def level2():
	print "~~~~~~~~~~~~~~~~~~~~~~~~~"
	print """

	Welcome to level 2 !!!

	"""





base_word = eight(check(raw_input("Type an eight letter word: ")))
typeFirst_mid()

