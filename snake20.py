from sys import argv 

script, input_file = argv
# a function to read the file held and open in the variable 'current_file' and then passed..
# the variable is passed to this functions's arguement
def print_all(f):
	print f.read()
# seek takes us to the begining of the file
def rewind(f):
	f.seek(0)
# we print the numer of the line we want to read and the we print the content of the line
# the comma makes sure the 'print' doesnt end with newline 
def print_a_line(line_count, f):
	print line_count, f.readline(),

current_file = open(input_file)

print "First let's print the whole file:\n"
# calling the function print_all'
print_all(current_file)

print "Now lets rewind, kind of like a tape"
# calling the function 'rewind'
rewind(current_file)

print "Let's print three lines:"
#calling functions
current_line = 1
print_a_line(current_line, current_file)
# current_line = 1 (initially) plus another 1. current lines = 2
current_line +=1
print_a_line(current_line, current_file)
# current_line = 2 (from the last global variable) plus another 1. current lines = 3
current_line +=1
print_a_line(current_line, current_file)