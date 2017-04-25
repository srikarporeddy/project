'''a = 5
b = 4
c = 3'''

# Uncomment below to take inputs from the user
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = float(( a + b + c ) / 2)

area = float((s*(s-a)*(s-b)*(s-c))**0.5)

print (area)