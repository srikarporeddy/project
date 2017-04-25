# shuffling cards we need to import random tools
import itertools, random

#make deck of cards
deck = list(itertools.product(range(1,14),['spade''heart','diamond','club']))

random.shuffle(deck)

print ("you got:")
for i in range(1,5):
	print(deck[i][0],"for", deck[i][1])
 