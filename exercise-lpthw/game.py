""" there are three doors inside which you have two doors each inside
which you have one doors each out of which on leads you out to safty
and the other two leads you back to the first doors. Find your way """

from sys import argv 

script, name = argv

line = "_"
dots = "." 
star = "*" #for demacation every new stage
air =  "~"
pointed = "^"
laoding = "|"
prompt = "Hit 'Enter' to continue: "
prompti = "Proceed?: "

storyLine = []


def Beginning():
	# print "previous moves:"
	# for i in storyLine:
	# 	print i

	""" the begining you have three routes to choose stage a_route """
	print star * 120
	print "WHICH WOULD BE WORSE, TO LEAVE AS A MONSTER OR DIE AS A GOOD MAN?\n\tSuddenly you are here. Yes just here. An end. You have three path - #1, #2 and #3"
	chooseRoute = raw_input("choose a path: ")
	storyLine.append(chooseRoute)
	while True:
		if chooseRoute == "1":
			a_routeOne(chooseRoute)
		elif chooseRoute == "2":
			a_routetwo()
		elif chooseRoute == "3":
			a_routeThree()
		elif not(chooseRoute == "1" and chooseRoute == "2" and chooseRoute == "3"):
			print "you did'nt choose the route available. choose again"
			Beginning()
		else:
			print "you are Dumb! choose a route!"
			Beginning()

def a_routeOne(chosedRoute):
	print "Who dares to walk this path - %s." % chosedRoute
	name = raw_input(" ^(-_-)^  Halt! Declare yourself 'Enter name': ")
	print line * 120
	print "The hardest walk you can make is alone. But it's the walk that will make you stronger"
	print "%s, There are two path to take from here- #1 or #2" % name
	print """
	Choose the wrong path and be devoured by the floor beneath your feet hahahahahah!!!
	Choose the right path and be granted passage into valhalla.
	No going back! Welcome to your fears!!!  (lightening and thunder strikes) ^(-`__'-)^ 
		"""

	chooseRoute_bi = raw_input("choose a route: ")
	storyLine.append(chooseRoute_bi)
	print line * 120

	if chooseRoute_bi == "1":
		print "\tThere is a gun in your pocket. Its not loaded but you'll die if you pull the trigger."
		print "\tNow choose either to shoot yourself or be consumed by the floor beneath your feet"

		die_by = raw_input(" ^(-`__'-)^ Die by the Gun or the Floor. It's up to you.: ")
		storyLine.append(die_by)
		if die_by == "gun":
			print "** you brought out the gun and pointed it at your head **"
			raw_input("Press 'Enter' to pull the triger: ")
			print " __'a very loud sound'__"
			print "THE END. ...the gun was loaded."

			print """
			~`Return to the earth now if your mind is troubled and your heart is unsettled'~
			~'For it is by returning to the beginning that we can clearly see the path'~
			"""
			raw_input("'Enter' to return to the 'EARTH': ")
			Beginning()
		elif die_by == "floor":
			print """%sYou chose the monster beneath you!, The gun was not loaded you really wanted to die. """ % (air * 5)
			print "**The floor beneath your feet opens and devours you**.\nTHE END"
			print "\t\tLIFE TIP: When faced with a dead end return to the beginning to clearly see the path and find your way."
			raw_input("'Enter' return: ")
			Beginning()
		else: 
			"%s must be dumb!" % name
			a_routeOne(chosedRoute)

	elif chooseRoute_bi == "2":
			print "You have been granted passage in the next realm to behold the face of Odin."
			raw_input("To proceed use you have been instructed by the gods to 'Enter' with your middle finger: ")
			b_routei()
	else:
		print "Are you mad?? simple thing choose one route!ahn ahn!!!"
		a_routeOne(chosedRoute)


def b_routei():
	print """
	Welcome to Asgard!!! ...may the force be with you. \n**the path which brought you here disapears**.
	You are in a new beginning with just a door that leads to...**
		"""
	raw_input("'Enter' to find out: ")

	print """
	A DEAD END! hahaha!!. You cannot return. Wait for death.

	...life is hard death is bliss.
	we struggle through life in search for peace, rest, and immortality
	we get hurt, troubled, become faint and weak.
	we keep on struggling, as a result we get old and feeble.
	then find immortality, peace and rest effortlessly in death.
	Death is bliss...

	"""
	print "**The valkyries leads your soul to the hall of the chosen dead**"
	raw_input("'Enter' to find immortality: ")
	Beginning()


def a_routetwo():
	print pointed * 120
	print "\t**a feminine voice speaks softly**"
	print " 'There is unrest here. You seek a way out of this widerness' "
	print " \t**Darkness befalls you**."
	print "%s!!! You must be brave. How dare you!!! mere mortal! step into this realm!" % name
	print "...unless of course you choose the right path you shall live"

	chooseRoute_bii = raw_input("choose now and decide your faith #1 or #2?: ")
	storyLine.append(chooseRoute_bii)
	if chooseRoute_bii == "1":
		print "\tTHE ROAD ENDS HERE FOR YOU"
		print "**%s runs mad and hung him self. He was caused by the goddess of snakes**" % name
		print "**He finds no rest in death. For this widerness imprisons both the body and the soul."
		print "\tHe who fights and runs away, lives to fight another day - THE GODDESS OF SNAKES"
		raw_input("Your spirit searches for peace, for a way out of this widerness for death is no freedom here 'Enter': ")
		Beginning()
	elif chooseRoute_bii == "2":
		print star * 120
		print "**you are walking on a rough road tired and thirsty. Then you met an angel**"
		print "\tAngel: Do not be afraid!. You have fought a good fight. You have finished the race. You have kept the faith. The crown of salvation awaits you"
		print "**Angel continues** ...raise your hands to the sky and pay homage."
		raw_input("**you did as you've been told 'Enter: ")
		print "\t....You have summond the sun god 'Ra' he sees all things"
		print "\tyou have two choices worship the sun god or follow me. My dear. I will find a way for you."
		b_routeii()
	else:
		print "Are you mad?? simple thing choose one route!ahn ahn!!"
		raw_input("'Enter' to choose again: ")
		a_routetwo()

def b_routeii():
	follow = raw_input("The sun or the angel: ")
	storyLine.append(follow)
	if follow == "sun":
		print line * 120
		print """
			With every sun comes a new day.
			A new beginning.
			A hope that things will be better today
			than they were yesterday.
			"""
		print """
			You Didn't hide.
			You have decided to Live.
			Now follow the sun.
			You'll make out of the wilderness.
			You followed the light, HE that sees all things -right choice.
			"""
		print """ 
			There it is! The sun!
			You have done it!
			Follow the sun and ride on it to 'Tomorrow!
			Run!
			"""
		print "YOU WIN."
		raw_input("Congratulations! 'Enter' End game\nWarning: Don't play again. You might, no will lose: ")
		exit(0)
	elif follow == "angel":
		print air * 40
		print "NOW I SHALL REVEAL MY TRUE SELF. Good afternoon, good evening, and good night!"
		print "**The angle turns into a lion with three heads and a tail of seven snakes**\n"
		print "\tDemon: I was fair. Now he is all mine.\n\t **a voice in wilderness**: Do with him as you please"
		print line * 120
		print "-WRONG CHOICE TO DEAD END-"
		raw_input("'Enter' To remake choices: ")
		Beginning()
	else:
		print "Are you mad?? simple thing choose one angel or sun !ahn ahn!!"
		raw_input("Enter to choose again: ")
		b_routeii()


def a_routeThree():
	print star * 120
	print "If there is a presence in this path give us a sign"
	raw_input("Give a sign 'Enter': ")
	name = raw_input("declare your name to the spirits: ")
	print "\t%s! My name is Ozymandias, king of kings: Look on my works, ye Mighty, and despair!" % name
	print "'You have been guilded into this realm by my creations, though you do not see them - the creatures of light!'"
	print "'A dark presence exits. It bekons. Careful the choices you make'"
	raw_input("***voice fades into the background*** 'Enter'")
	print line * 120
	print "You have two choices darkness or light. Which is your ally? "

	chooseRoute_biii = raw_input("darkness or light: " )
	storyLine.append(chooseRoute_biii)
	if chooseRoute_biii == "darkness":
		print laoding * 120
		print "**A voice in the dark**: 'Ah!! you think darkness is your ally? You merely adopted the dark. \nI was born in it, molded by it."
		print "I didn't see the light until I was already a man,... \nby then it was nothing to me but blinding!"
		print "\tYou can't find True where there is False. Even if True or False is True.  \n\tTrue and False is False. "
		print "\tCause the two can't coexist simultaneously and can never meet like light and darkness. - iPrime \n**Ozymandias has decided your faith long ago** "
		print line * 120
		raw_input("'Enter' to receive judgment: ")
		print "YOU ARE DOOMED!!! \nThere's no light at the end of this tunnel."
		Beginning()

	elif chooseRoute_biii == "light":
		print "**You have entered the fortress of Ozymadias**"
		print "'child of light! you have chosen well!' \nI feel your chakra, your light shines well into the next dimension"
		print "loading%s" % (dots * 113)
		raw_input("proceed to the world beyond: 'Enter'")
		b_routeiii()

	else:
		print "oya choose your head naw. wehrey!"
		raw_input("hit enter start afresh: ")
		a_routeThree()


def b_routeiii():
	print "**You are at the foot of Ozmandias.**"
	raw_input("put your right hand on your chest and recite: 'Enter'")
	print """
	I do not aim with my hand; he who aims with his hand has forgotten the face of his father.
	I aim with my eye.

	I do not shoot with my hand; he who shoots with his hand has forgotten the face of his father.
	I shoot with my mind.

	I do not kill with my Gun; he who kills with his gun has forgotten the face of his father.
	I kill with my heart.
   	"""
   	print line * 120
   	raw_input("'Enter' to continue: ")
   	print "Ozymandias: Your light outshines you. Your chakra is overwhelming. And you have forgotten the face of your father!"
   	print "Your light betrays you. It was never your ally. You have been spotted by darkness.\nDEAD END!!"
   	print "Your light waited long enough it took it time. Your light was a silent guardian. A watchful protector. A Dark Knight, YOUR DOOM!"
   	print "Your light was born of darkness"
   	raw_input("'Continue': ")
   	print pointed * 100
   	print """
   	Its the slow knife, the knife that takes its time, 
   	the knife that waits years without forgetting, then slips quietly between the bones. 
   	Thats the knife that cuts the deepest
   	....Today is a good day to die.
   	"""
   	raw_input('White knight arise! "Enter"')
   	Beginning()




print "loading%s 45percent" % (dots * 50)
raw_input(prompt)
print "Listen carefully Let me tell you a little story."
raw_input(prompti)

print """
%s
Until death ...as far back as I can remember, I always wanted to be a gangster.
You don't need my name. I am the commander of the Armies of the Underworld, General of the Legions of Doom
and loyal servant of death. Father to a murdered son, husband to a murdered wife.\nAnd I will have my vengeance, in this life or the next.
I am but a wondering spirit taking forms.
""" % (laoding * 120)
raw_input(prompt)
print star * 120
print "THE BEGINNING"
print "***'The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air.'***"
print "ARE YOU WATCHING CLOSELY?."
print "The journey to an unknown end begins.... and where you're going, you don't need roads"
print "...may the odds ever be in your favour"
print "loading%s 100percent\ncomplete!" % (dots * 100)
raw_input("'Press Enter' :")
Beginning()

