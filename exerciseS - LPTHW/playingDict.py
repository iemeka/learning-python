
# letter = {
# 	'a': ["anabel","aboki","alabukun","alabosi"],
# 	# 'b': ["betnija","babablue","bleble","biscuit"],
# 	# 'c': ["cowbel","casala","cassava","case-study"]
# }

# A = letter["a"]


# meaningA = {
# 	A[0]: "a name of a girl",
# 	A[1]: "man from the north",
# 	A[2]: "nigerian cocain",
# 	A[3]: "to kabalize somebody or when one cant stop talking"
# }


# for word, mean in meaningA.items():
# 	print word, mean

# for val in meaningA.keys():
# 	print ". .".join(val)


# letter.update(meaningA)

# print letter

#set

A = {x: x for x in range(1, 10) if x%2==0}
C = [x for x in range(1, 10) if x%2==0]

B = [y for y in range(1, 10) if y%2!=0]
print "dictionary"
for i in A:
	print(A[i])

print "list"
r = 0
for ii in C:
	print(C[r])
	r +=1