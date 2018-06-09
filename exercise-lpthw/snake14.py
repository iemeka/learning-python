from sys import argv

script, user_name, code = argv
prompt = '~/:-'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "what programming language are you currently learning... %s" % code
program = raw_input("??? wow!! cool")

print """
Alright, do you said %r about liking me.
You live in %r. Not sure where that is though.
And you have a %r computer. Awesome.
well use it wisely and learn to write %s
""" % (likes, lives, computer, code)