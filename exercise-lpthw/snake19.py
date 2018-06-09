# def cheese_and_crackers(cheese_count, boxes_of_crackers): #defined a function with two arguements
# # the arguements acts as variables and takes different values which are embeded in the script
# 	print "You have %d cheeses!" % cheese_count
# 	print "You have %d boxes of crackers!" % boxes_of_crackers
# 	print "Man tha's enough for party!"
# 	print "Get a blanket. \n"

# print "We can just give the function numbers directly:"
# cheese_and_crackers(20, 30)

# # declared a variable and used to call the function

# print "OR, we can use variables from our script:"
# amount_of_cheese = 10 
# amount_of_crackers = 50
# # passing the values of the variable into the fuction
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print "We can even do math inside too:"
# # passing nuber values into the fuction
# cheese_and_crackers(10 + 20, 3 + 4)

# print "And we can combine the two, variables and math:"
# # passing both number and variable values into the function while calling it
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10000)



# CLASS WORK
from sys import argv
script, call_male, call_female = argv

def human_being(male, female):
	print "%s %s \n" % (male, female)


human_being("boy","girl")

strong = "man"
stronger = "woman"
human_being(strong, stronger)

Name_male = raw_input("name a boy- ")
Name_female = raw_input("name a girl- ")
human_being(Name_male, Name_female)

human_being(call_male, call_female)

human_being(1 + 4, 5 + 0)


book = open("form.txt").read()
new = open("snake19.py").read()
human_being(book, new)

human_being(stronger, 4)

human_being(strong, "strong")

male = 5 < 7
female = 5 > 7
human_being(male, female)

human_being(strong + stronger, "stronger" + "strong")
