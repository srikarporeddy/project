## contacts program using classes

"""
 this person class defines a person in terms of name, phone , email adresss

"""
class Person(object):
		
			
	#constructor
	def __init__(self, theName, thePhone, theEmail):
		self.name = theName
		self.phone = thePhone
		self.email = theEmail
	#accesori methods(getters)
	def getName(self):
		return self.name
	def getPhone(self):
		return self.phone
	def getEmail(self):
		return self.email
	#mutators methods(setters)
	def setPhone(self, Newphonenumber):
		self.phone= Newphonenumber
	def setEmail(self, NewEmailadress):
		self.email= NewEmailadress
	def __str__(self):
		return "person[name= "+self.name +\
				",phone= "+self.phone +\
				",email=   "+self.email+\
				"]"

def enter_a_friend():
	name = input("Enter friends name: ")
	phone = input("Enter phone number ")
	email = input("Enter Email address: ")
	return Person(name, phone, email)
def lookup_a_friend(friends):
	found = False
	name = input(" Enter name to lookup: ")
	for friend in friends:
		if name in friend.getName():
			print(friend)
			found = True
	if not found:
		print(" no friend is on that name :")

def show_all_friends(friends):
	print("showing all contacts")
	for friend in friends:
		print (friend)

def main():
	friends = []
	running = True
	while running:
		print("\nContacts Manager")
		print("1. New contact 2. lookup")
		print("3. Show contacts 4. end ")
		option = input(">>>")
		if option == "1":
			friends.append(enter_a_friend())
		elif option == "2":
			lookup_a_friend(friends)
		elif option == "3":
			show_all_friends(friends)
		elif option =="4":
			running = False
		else:
			print("Unrecognized input please try again:")
	print("program ending...")

if __name__=="__main__":
	main()



