#!/usr/bin/python2.7

import sys

f = open('common.dict','r')

commonwords = {}

for line in f:
	commonwords[line.strip()] = 1

f.close()

for line in sys.stdin:

	tweet = line.split()

	rules = {}

	rules["RT"] = 1
	rules['@'] = 1
	rules['#'] = 1

	rejects = []

	for word in tweet:
		try:
			if rules[word[0]] or rules[word]:
				rejects.append(word)
		except:
			continue

	for word in rejects:
		tweet.remove(word)
		
	score = 0

	for word in tweet:
		try:
			score += commonwords[word]
		except:
			continue
	if score < 2:
		continue

	final = ""

	for word in tweet:
		final = final + " " + word
	print final

