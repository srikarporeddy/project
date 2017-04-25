x = int(input(" please enter the number : "))

listrange = list(range(1, x+1))

newlist = []

for i in listrange:
	if x % i == 0:
		newlist.append(i)
print(newlist)

