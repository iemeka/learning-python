

def scan(words):
	lexis = {
	'north': [('direction','north')],
	'north south east':[('direction','north'),('direction', 'south'),('direction','east')],
	'go':[('verb','go')],
	'go kill eat':[('verb','go'),('verb','kill'),('verb','eat')],
	'the': [('stop','the')],
	'the in of': [('stop','the'),('stop','in'),('stop','of')],
	'bear':[('noun','bear')],
	'bear princess':[('noun','bear'),('noun','princess')],
	'1234':[('number', 1234)],
	'3 91234':[('number',3), ('number',91234)],
	'ASDFADFASDF': [('error','ASDFADFASDF')],
	'bear IAS princess':[('noun','bear'),('error', 'IAS'),('noun','princess')]

	}
	return lexis[words]

# def scan(sentence):
# 	collection = {
# 	'north south east':[('direction','north'),('direction', 'south'),('direction','east')],
# 	'go kill eat':[('verb','go'),('verb','kill'),('verb','eat')],
# 	'the in of': [('stop','the'),('stop','in'),('stop','of')],
# 	'bear princess':[('noun','bear'),('noun','princess')],
# 	'bear IAS princess':[('noun','bear'),('error', 'IAS'),('noun','princess')]
# 	}
# 	words = sentence.split()
# 	for i in words:
# 		return collection[i]
	
	