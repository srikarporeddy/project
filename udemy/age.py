def age_in_sec():
	user_input = input("Enter your age: ")
	seconds = int(user_input)*12*24*60*60
	print("you have lived for {},seconds".format(seconds))
age_in_sec()
def divisible():
    user_input=input("Enter your number:")
    divide=input("Enter divisor: ")
    divisor=int(user_input)/int(divide)
    print("the divisor of given number is {}".format(divisor))
divisible()
def age_program():
	seconds_or_years=input("Give me seconds (s) or years (y):  ")
	if seconds_or_years == "s":
		user_value=input("no of seconds lived for:")
		print("you have lived for {} this many years".format(int(user_value)/60/60/24/365))
	elif seconds_or_years == "y":
		user_value=input("no of years lived for:")
		print("you have lived for {} this many seconds".format(int(user_value)*60*60*24*365))
age_program()


	# Ask the user for a number.
	# Print "It's even" if the number is even, or "It's odd" otherwise.
	# (make sure to convert the user input to an integer!)
	# You can use the divisible() method if you wish.
