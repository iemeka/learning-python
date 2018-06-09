from sys import argv

script, file = argv

prompt = "$$- "

print "Hello!"
name = raw_input("please enter your name %s" % prompt) 
print "Welcome %s. How are you?" % name
doing = raw_input(prompt)
print "Nice to know you're %s" % doing
print "I am going to ask a few questions about you if that's ok?"
print "Type 'ok' otherwise press crtl-c"
raw_input(prompt)
print "Thanks for obliging %s" % name
print "Loading questions....."
raw_input("\"Hit 'enter' to continue\"")
print "what are your other names ?"
otherNames = raw_input(prompt)
print "what is the name of your school?"
school = raw_input(prompt)
Address = raw_input("home address %s" % prompt)

print "That will be all for now. Thanks\nReports loading...."

open_file = open(file, "w")

open_file.write(("%s\n%s\n%s\n%s\n%s") % (name, doing, otherNames, school, Address))

open_file.close()