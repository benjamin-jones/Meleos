#!/usr/bin/python2.7
import sys, time

class EmotionVector:
	def __init__(self):
		self.joy = 0
		self.trust = 0
		self.fear = 0
		self.surprise = 0
		self.sadness = 0
		self.disgust = 0
		self.anger = 0
		self.anticipation = 0
	def __add__(self,y):
		r = EmotionVector()
		r.joy = self.joy + y.joy
		r.trust = self.trust + y.trust
		r.fear = self.fear + y.fear
		r.surprise = self.surprise + y.surprise
		r.sadness = self.sadness + y.sadness
		r.disgust = self.disgust + y.disgust
		r.anger = self.anger + y.anger
		r.anticipation = self.anticipation + y.anticipation
		return r
	def __sub__(self,y):
                r = EmotionVector()
                r.joy = self.joy - y.joy
                r.trust = self.trust - y.trust
                r.fear = self.fear - y.fear
                r.surprise = self.surprise - y.surprise
                r.sadness = self.sadness - y.sadness
                r.disgust = self.disgust - y.disgust
                r.anger = self.anger - y.anger
                r.anticipation = self.anticipation - y.anticipation
                return r

f = open('joy.dict','r')
joylist = []
for line in f:
	joylist.append(line.strip());

runningAvgList = []

for line in sys.stdin:
	line = line.strip()
	evector = EmotionVector()
	tweet = line.split()
	for word in tweet:
		word = word.strip()
		evector.joy += joylist.count(word)
	if len(runningAvgList) < 100:
		runningAvgList.append(evector.joy)
	else:
		runningAvgList.pop(0)
		runningAvgList.append(evector.joy)
		print str( sum(runningAvgList) / 100.0 ) 
		
