#declared a variable, assigning the string value to it.
#embedded in the string is a format character whose value is a number 10 assigned to it
x = "There are %d types of people." % 10
#declared a variable assigning to it the string value
binary = "binary"
#same as above
do_not = "don't"
# also same as above but with who format characters whose values variables
# hence the value of the two format characters equals the value of the two variables assigned to the format character
y = "Those who know %s and those who %s." % (binary, do_not)
# told python to print the values of the variable x
print x
# told python to print the values of the variable y
print y
# here python has the print a string in which a format character is embedded and whose value is he
# the values of he variable x
print "I said: %r." % x
# same here ...which value is the values of the variable y
print " I also said: '%s'. " % y

#assigned a boolean to a variable
hilarious = False
# declared a variable assigning assigning to it a string with an embedded format character
joke_evaluation = "Isn't that joke so funny?! %r"
# told python to print the value of the variable which is a string which a format character
# is embedded in it then assigning the value of the embedde character in the string the value
# of another variable.
# so python has to print a variable value assigning a variable to the format character in the first variable value
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
# here python simply joined two stings together using the operator + thats why is makes 
# a longer string. In javaScript is called concatenation of strings (learnt javaScript initially) tongue out* <(-,-)>
print w + e


# yes! they are four places fuck you shaw!