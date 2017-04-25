s = input("please enter a word to check palindrome:")
p= str(s)
r= s[::-1]
print(r)
if p == r:
	print(s,"is a palindrome")
else:
	print(s,"is not a palindrome")


def reverse(word):
	x = ' '
	for i in range(len(word)):
		x += word[len(word)-1-i]
		return x
word = input("give me a word:\n")
if x == reverse(word):
	print(word," is palindrome")
else:
	print(word,"is not a palindrome")