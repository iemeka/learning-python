from sys import argv

hey, script, name, school, ambition = argv
prompt = ">>> "
print "name pls"
text1 = raw_input((prompt + "%s. Correct? ") % name)
print "school??"
text2 = raw_input((prompt + "%s. Correct? ") % school)
print "future ambition"
text3 = raw_input((prompt + "%s. Correct? ") % ambition)

file = open(script,"w+")
file.write(("%s %s\n%s %s\n%s %s") % (text1, name, text2, school, text3, ambition))
file.close()
print "script %s loading..." % script
raw_input(prompt + "hit enter to continue")

learn = open(script)
see = learn.read()

print see

