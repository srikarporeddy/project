def lcm(x,y):
	""" this functions takes two integers and return L>C>M"""
	if x>y:
		greater = x
	else:
		greater = y
	while(True):
		if((greater %x==0) and (greater %y==0)):
			lcm = greater
			break
		greater += 1
	return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print (lcm(num1,num2))