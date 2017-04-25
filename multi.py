
for i in range(99, 0, -1):
        if i == 1:
                print('1 bottle of beer on the wall, 1 bottle of beer!')
                print('So take it down, pass it around, no more bottles of beer on the wall!')
        elif i == 2:
                print('2 more bottles of beer on the wall, 2 more bottles of beer!')
                print('So take one down, pass it around, 1 more bottle of beer on the wall!')
        else:
                print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
                print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))


11:46
'''
Python Training

data_list_3 = []
data_list_5 = []

result = 0

for data in range(1, 1001):
    if data % 3 == 0:
        data_list_3.append(data)
    
    if data % 5 == 0:
        data_list_5.append(data)


for x in data_list_3:
    result = result + x

for x in data_list_5:
    result = result + x
print(result)



                '''#range = [1, 2, 3, 4, 5]
my_new_list = []
#for i in my_list:
  for i in range(3, 6):
    my_new_list.append(i * 5)

print(my_new_list)


#[5, 10, 15, 20, 25]
#for i in range(3, 6):
#...     print(i)


my_list = [1, 2, 3, 4, 5]

list = [i * 5 for i in my_list

 print list


multiples =[x**2 for  x in range(1000)]
for i  in multiples:
print i '''

'''def multiples(3, count):
    for i in range(1000):
        print(i*3)
       # print range(0, (m+3), n)
       #max = 1000  
for  i in range(0,max):
if i%3 == 0 
#or i%5 == 0:
    result += i

print result
name = "srikar"
array = [1, 2, 3, 4, 5]
 
for data in array:
    print(data)

for data in name:
    print(data)
for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
      '''
