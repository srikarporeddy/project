a = [1,1,2,3,3,5,8,13,34,55,89]
b = [1,2,3,4,5,6,7,8,9,0,13,11,12,13]


'''print([a,b])
c=[]
c.append(a)
print(c)
c.insert(b)
print(c)'''


#s=list(set(a).intersection(b))
#print(s)

def common_element(a,b):
	result =[]
	for element in a:
		if element in b:
			#if a not in result:
			result.append(element)

	print (set(result))
common_element(a,b)

#!/bin/python
import random

#compute random lists
randa = []
randb = []

for a in range(0,40):
    a = random.randint(0,40)
    randa.append(a)
for b in range(0,40):
    b = random.randint(0,40)
    randb.append(b)

#remove duplicates on the random lists
rand_a = set(randa)
rand_b = set(randb)

#compare the two random lists
match = []
for check1 in rand_a:
    #if (check1 in rand_b) == True:
    match.append(check1)
print (set(match))