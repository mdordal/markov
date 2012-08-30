import itertools
from random import randint, choice

def generateMarkovDict(text, n):
	'''generate a markov dictionary from text, using n words as state'''
	markovDict = {}
	# preload the n-tuple
	state = tuple(itertools.islice(text, n))
	start = state

	for word in text:
		if state not in markovDict:
			markovDict[state] = {'sum': 0, 'words':{}}
		data = markovDict[state]
		if word in data['words']:
			data['words'][word] += 1
		else:
			data['words'][word] = 1
		data['sum'] += 1
		state = state[1:] + (word,)
	for word in start:
		if state not in markovDict:
			markovDict[state] = {'sum': 0, 'words':{}}
		data = markovDict[state]
		if word in data['words']:
			data['words'][word] += 1
		else:
			data['words'][word] = 1
		data['sum'] += 1
		state = state[1:] + (word,)
	return markovDict

def genText(markovDict, length):
	seed = list(markovDict)[randint(0, len(markovDict) - 1)]
	state = seed
	output = []
	output += seed
	for i in range(length):
		if state not in markovDict:
			print state
			raise
		data = markovDict[state]
		choice = randint(0, data['sum'] - 1)
		for word, weight in markovDict[state]['words'].iteritems():
			choice -= weight
			if choice < 0:
				state = state[1:] + (word,)
				output.append(word)
				break
	return output

def pretty(md, ln):
	print ' '.join(genText(md, ln))

f = open('grey', 'r')
corpus = f.read().replace('\n', ' ').replace('\t', ' ').replace('  ', ' ').replace('  ', ' ')

m1 = generateMarkovDict(corpus.split(' '), 1)
m2 = generateMarkovDict(corpus.split(' '), 2)
m3 = generateMarkovDict(corpus.split(' '), 3)
m4 = generateMarkovDict(corpus.split(' '), 4)
