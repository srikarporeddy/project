for i in range (1,11):
	print (i)
	if i==5:
		
		print(i)
		break
if True:
	print("hello")

a = 5
print(a,"is of type", type(a))
a = 2.0
print(a,"is of type",type(a))
a = 1+2j
print(a, "is of type",type(a))

#list
a = [5,10,15,20,25,30,35,40,45,50]
print("a[2]=",a[2])
print("a[0:3]=",a[0:3])
print("a[5:]=",a[5:]) 
#mutable
a =[1,2,3]
a[2]=5
print(a)

#tuple
t = (5,'program',1+3j)
print("t[1]=",t[1])
print("t[0:3]=",t[0:3])
#strings
s = 'hello world'
print(s)
#strings are immutable
#sets
a = {1,2,3,4,5,6,7,6}
print("a=",a)
a = {1,1,1,2,2,2,3,3,3,4,4,4,4}
print("a=",a)
list('hello')
print(list)


