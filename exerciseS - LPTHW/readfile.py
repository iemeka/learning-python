from sys import argv

script, filename = argv

store = open(filename)

print store.read()