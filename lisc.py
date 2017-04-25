a = [1,2,3,4,5,6,7,8,9,0,12,13,14,12,16]
b=[number for number in a if number % 2==0]
print(b)

import random 
numlist = []
list_length = random.randint(5,25)

while len(numlist) < list_length:
	numlist.append(random.randint(1,75))
evenlist = [number for number in numlist if number %2== 0]
print(numlist)
print(evenlist)