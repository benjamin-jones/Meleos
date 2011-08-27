#!/usr/bin/python2.7

import sys

files = []

for arg in sys.argv:
	if arg == "./Preprocessing.py":
		continue;
	files.append(arg);

for file in files:
	f = open(file, 'r')

	for line in f:

		tweet = line.split()

		rules = []

		rules.append(["RT",'i'])
		rules.append(['@','b'])
		rules.append(['#','b'])

		rejects = []

		for word in tweet:
			for rule in rules:
				if rule[1] == 'i':
					if word == rule[0]:
						rejects.append(word)
				if rule[1] == 'b':
					if word[0] == rule[0]:
						rejects.append(word)

		for word in rejects:
			tweet.remove(word)

		final = ""

		for word in tweet:
			final = final + " " + word
		print final			
