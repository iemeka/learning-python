# takes arguments from the system when the script is runned
# from sys import argv
# # assigns variables to the arguments respectively
# script, filename = argv
# # got a file imported as an argument stored in a variable which is apparently being stored in another variable
# txt = open(filename)
# # prints the name of the file
# print "Here's your file %r" % filename
# # reads the file stored in the variable
# print txt.read()
# txt.close()
# heres another way we can do it
print "Typed the filename again:"
# get a string through user input, store it in a variable
file_again = raw_input("> ")
# the string is a filename which has been contained and stored in a variable
txt_again = open(file_again)
# now we print the content of the file.
print txt_again.read()
txt_again.close()