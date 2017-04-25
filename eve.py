'''
num = input("Enter a number: ")

i= float(num) % 2 

if i == 0:
	print("the given number is even")
else :
	print("the given number is odd ")
'''

number = int(input("give me a number to check: "))
check = int(input("give me number to divide: "))

#j = float(number) % 4
if number % 4 == 0:
	print(number," is a nultiple of 4")
elif number % 2 == 0:
	print(number, " is an even number")
else:
	print(number,"the number is odd ")
 
if number % check == 0:
	print(number, "divides by ", check)
else:
	print(number,"doen't divide even by", check)
