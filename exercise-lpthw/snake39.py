# create a mapping of state to abbreviation
import collections

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'

}

# create a basic set of states an some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities["NY"] = "New York"
cities['OR'] = 'Portland'

# print out some cities
print "_" * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '_' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using state then cities dict
print "_" * 10
print "Michigan has: ",cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation

print "_" * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '_' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print "_" * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

print type(states)
print len(cities)



dictor = [
	('mans', 'womans'),
	('hey', 'nah!'),
	('cool', 'hot'),
	(55, 56)
]

dictor = collections.OrderedDict(dictor)
for i in dictor:
	print dictor[i]
	if dictor[i] == 'hot':
		print dictor[2]


# fat = collections.OrderedDict()

# fat[45] = 54
# fat[35] = 53
# fat[4849] = 0
# fat[65] = 56
# fat[40] = 04

# for o,p in fat.items():
# 	print o , p
